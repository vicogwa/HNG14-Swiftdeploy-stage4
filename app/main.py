import os
import time
import random
import threading
from flask import Flask, request, jsonify, make_response, Response
from prometheus_client import (
    Counter, Histogram, Gauge,
    generate_latest, CONTENT_TYPE_LATEST, REGISTRY
)

app = Flask(__name__)

START_TIME = time.time()
MODE = os.environ.get("MODE", "stable")
VERSION = os.environ.get("APP_VERSION", "1.0.0")

# ── Prometheus metrics ────────────────────────────────────────────────────────
# Counts every HTTP request, labelled by method, path, and status code.
# Example: http_requests_total{method="GET",path="/healthz",status_code="200"} 42
http_requests_total = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "path", "status_code"]
)

# Measures how long each request took, bucketed into ranges (histogram).
# Buckets: 5ms, 10ms, 25ms, 50ms, 100ms, 250ms, 500ms, 1s, 2.5s, 5s, 10s
http_request_duration_seconds = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "path"],
    buckets=[0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
)

# A gauge is a single number that goes up or down.
app_uptime_seconds = Gauge("app_uptime_seconds", "Seconds since app started")
app_mode = Gauge("app_mode", "Current mode: 0=stable, 1=canary")
chaos_active = Gauge("chaos_active", "Chaos state: 0=none, 1=slow, 2=error")

# ── Chaos state ───────────────────────────────────────────────────────────────
_chaos = {"mode": None, "duration": None, "rate": None}
_chaos_lock = threading.Lock()


def _update_gauges():
    """Keep Prometheus gauges in sync with current runtime state."""
    app_uptime_seconds.set(round(time.time() - START_TIME, 2))
    app_mode.set(1 if MODE == "canary" else 0)
    with _chaos_lock:
        m = _chaos["mode"]
    chaos_active.set(0 if m is None else (1 if m == "slow" else 2))


# ── Middleware: record every request ─────────────────────────────────────────
@app.before_request
def _before():
    request._start_time = time.time()


@app.after_request
def _after(response):
    # Skip recording the /metrics endpoint itself to avoid noise
    if request.path != "/metrics":
        duration = time.time() - request._start_time
        http_requests_total.labels(
            method=request.method,
            path=request.path,
            status_code=str(response.status_code)
        ).inc()
        http_request_duration_seconds.labels(
            method=request.method,
            path=request.path
        ).observe(duration)
    return response


# ── Helpers ───────────────────────────────────────────────────────────────────
def _build_response(data, status=200):
    resp = make_response(jsonify(data), status)
    if MODE == "canary":
        resp.headers["X-Mode"] = "canary"
    return resp


def _apply_chaos():
    with _chaos_lock:
        mode = _chaos["mode"]
        duration = _chaos["duration"]
        rate = _chaos["rate"]
    if mode == "slow" and duration:
        time.sleep(duration)
    elif mode == "error" and rate is not None:
        if random.random() < rate:
            return _build_response({"error": "chaos-induced error", "code": 500}, 500)
    return None


# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    chaos_resp = _apply_chaos()
    if chaos_resp:
        return chaos_resp
    return _build_response({
        "message": f"SwiftDeploy service running in {MODE} mode",
        "mode": MODE,
        "version": VERSION,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    })


@app.route("/healthz")
def healthz():
    _update_gauges()
    return _build_response({
        "status": "ok",
        "mode": MODE,
        "version": VERSION,
        "uptime": round(time.time() - START_TIME, 2),
    })


@app.route("/metrics")
def metrics():
    """
    Prometheus scrape endpoint.
    Returns all registered metrics in the Prometheus text exposition format.
    Example output line:
      http_requests_total{method="GET",path="/",status_code="200"} 5.0
    """
    _update_gauges()
    return Response(generate_latest(REGISTRY), mimetype=CONTENT_TYPE_LATEST)


@app.route("/chaos", methods=["POST"])
def chaos():
    if MODE != "canary":
        return _build_response({"error": "chaos endpoint is only active in canary mode"}, 403)

    body = request.get_json(silent=True)
    if not body or "mode" not in body:
        return _build_response({"error": "request body must include 'mode'"}, 400)

    chaos_mode = body["mode"]
    with _chaos_lock:
        if chaos_mode == "recover":
            _chaos.update({"mode": None, "duration": None, "rate": None})
        elif chaos_mode == "slow":
            duration = body.get("duration")
            if not isinstance(duration, (int, float)) or duration < 0:
                return _build_response({"error": "'duration' must be a non-negative number"}, 400)
            _chaos.update({"mode": "slow", "duration": duration, "rate": None})
        elif chaos_mode == "error":
            rate = body.get("rate")
            if not isinstance(rate, (int, float)) or not (0 <= rate <= 1):
                return _build_response({"error": "'rate' must be a float between 0 and 1"}, 400)
            _chaos.update({"mode": "error", "duration": None, "rate": rate})
        else:
            return _build_response({"error": f"unknown chaos mode: '{chaos_mode}'"}, 400)

    return _build_response({"chaos": "applied", "active_mode": chaos_mode})


if __name__ == "__main__":
    port = int(os.environ.get("APP_PORT", 3000))
    app.run(host="0.0.0.0", port=port)

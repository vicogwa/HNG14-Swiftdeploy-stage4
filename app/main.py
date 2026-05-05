import os
import time
import random
import threading
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

START_TIME = time.time()
MODE = os.environ.get("MODE", "stable")
VERSION = os.environ.get("APP_VERSION", "1.0.0")

# Chaos state — shared across threads
_chaos = {
    "mode": None,
    "duration": None,
    "rate": None,
}
_chaos_lock = threading.Lock()


def _build_response(data, status=200):
    resp = make_response(jsonify(data), status)
    if MODE == "canary":
        resp.headers["X-Mode"] = "canary"
    return resp


def _apply_chaos():
    """
    Apply active chaos configuration before responding.
    Returns a Flask response if chaos causes an error, else None.
    """
    with _chaos_lock:
        mode = _chaos["mode"]
        duration = _chaos["duration"]
        rate = _chaos["rate"]

    if mode == "slow" and duration:
        time.sleep(duration)
    elif mode == "error" and rate is not None:
        if random.random() < rate:
            return _build_response(
                {"error": "chaos-induced error", "code": 500}, 500
            )
    return None


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
    return _build_response({
        "status": "ok",
        "mode": MODE,
        "version": VERSION,
        "uptime": round(time.time() - START_TIME, 2),
    })


@app.route("/chaos", methods=["POST"])
def chaos():
    if MODE != "canary":
        return _build_response(
            {"error": "chaos endpoint is only active in canary mode"}, 403
        )

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
                return _build_response(
                    {"error": "'duration' must be a non-negative number"}, 400
                )
            _chaos.update({"mode": "slow", "duration": duration, "rate": None})
        elif chaos_mode == "error":
            rate = body.get("rate")
            if not isinstance(rate, (int, float)) or not (0 <= rate <= 1):
                return _build_response(
                    {"error": "'rate' must be a float between 0 and 1"}, 400
                )
            _chaos.update({"mode": "error", "duration": None, "rate": rate})
        else:
            return _build_response(
                {"error": f"unknown chaos mode: '{chaos_mode}'"}, 400
            )

    return _build_response({"chaos": "applied", "active_mode": chaos_mode})


if __name__ == "__main__":
    port = int(os.environ.get("APP_PORT", 3000))
    app.run(host="0.0.0.0", port=port)

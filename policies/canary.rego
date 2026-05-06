# policies/canary.rego
#
# Domain: Canary safety
# Question: "Is the canary healthy enough to promote to stable?"
#
# This policy checks error rate and P99 latency scraped from /metrics.
# Thresholds come from data.canary (loaded from policies/data.json).

package canary

import future.keywords.if
import future.keywords.contains

default allow := false

allow if {
    count(violations) == 0
}

violations contains msg if {
    input.error_rate > data.canary.max_error_rate
    msg := sprintf(
        "Error rate %.4f (%.2f%%) exceeds maximum %.2f%%",
        [input.error_rate, input.error_rate * 100, data.canary.max_error_rate * 100]
    )
}

violations contains msg if {
    input.p99_latency_ms > data.canary.max_p99_latency_ms
    msg := sprintf(
        "P99 latency %.1fms exceeds maximum %.1fms",
        [input.p99_latency_ms, data.canary.max_p99_latency_ms]
    )
}

decision := {
    "allow": allow,
    "violations": violations,
    "domain": "canary",
}

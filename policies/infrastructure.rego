# policies/infrastructure.rego
#
# Domain: Infrastructure health
# Question: "Is the host healthy enough to deploy to?"
#
# This policy checks disk space and CPU load.
# Threshold values come from data.infrastructure (loaded from policies/data.json)
# so you never need to touch this file to change limits.

package infrastructure

import future.keywords.if
import future.keywords.contains

# Default: deny unless explicitly allowed
default allow := false

allow if {
    count(violations) == 0
}

# Build a set of violation messages.
# Each `violations contains` block adds one message if its condition is true.

violations contains msg if {
    input.disk_free_gb < data.infrastructure.min_disk_free_gb
    msg := sprintf(
        "Disk free %.1fGB is below minimum %.1fGB",
        [input.disk_free_gb, data.infrastructure.min_disk_free_gb]
    )
}

violations contains msg if {
    input.cpu_load > data.infrastructure.max_cpu_load
    msg := sprintf(
        "CPU load %.2f exceeds maximum %.2f",
        [input.cpu_load, data.infrastructure.max_cpu_load]
    )
}

# The CLI reads this `decision` object — never a bare boolean.
decision := {
    "allow": allow,
    "violations": violations,
    "domain": "infrastructure",
}

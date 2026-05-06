# SwiftDeploy Audit Report

Generated: 2026-05-06 13:03:20 UTC

Total events recorded: 72

---

## Timeline

| Timestamp | Event | Detail |
|---|---|---|
| 2026-05-06 11:04:30 | teardown | Stack torn down |
| 2026-05-06 11:04:52 | deploy | Deployed in `stable` mode |
| 2026-05-06 11:20:16 | teardown | Stack torn down |
| 2026-05-06 11:20:38 | deploy | Deployed in `stable` mode |
| 2026-05-06 11:23:14 | teardown | Stack torn down |
| 2026-05-06 11:23:33 | deploy | Deployed in `stable` mode |
| 2026-05-06 11:26:03 | teardown | Stack torn down |
| 2026-05-06 11:26:11 | policy_violation | **BLOCKED** by `infrastructure` policy |
| 2026-05-06 11:28:07 | policy_violation | **BLOCKED** by `infrastructure` policy |
| 2026-05-06 11:28:49 | teardown | Stack torn down |
| 2026-05-06 11:29:05 | deploy | Deployed in `stable` mode |
| 2026-05-06 11:41:29 | promote | Promoted to `canary` |
| 2026-05-06 11:58:29 | status_scrape | rps=370.15  err=7.50%  p99=5.0ms  chaos=error |
| 2026-05-06 11:58:34 | status_scrape | rps=0.74  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 11:58:39 | status_scrape | rps=-0.79  err=7.50%  p99=5.0ms  chaos=error |
| 2026-05-06 11:58:44 | status_scrape | rps=0.97  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 11:58:49 | status_scrape | rps=0.20  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 11:58:54 | status_scrape | rps=0.00  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 11:58:59 | status_scrape | rps=-1.19  err=7.50%  p99=5.0ms  chaos=error |
| 2026-05-06 11:59:04 | status_scrape | rps=1.18  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 11:59:10 | status_scrape | rps=-0.99  err=7.32%  p99=5.0ms  chaos=error |
| 2026-05-06 11:59:15 | status_scrape | rps=0.20  err=7.14%  p99=5.0ms  chaos=error |
| 2026-05-06 11:59:20 | status_scrape | rps=0.00  err=7.14%  p99=5.0ms  chaos=error |
| 2026-05-06 11:59:25 | status_scrape | rps=0.79  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 11:59:30 | status_scrape | rps=0.00  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 11:59:35 | status_scrape | rps=-0.59  err=6.98%  p99=5.0ms  chaos=error |
| 2026-05-06 11:59:40 | status_scrape | rps=0.00  err=6.98%  p99=5.0ms  chaos=error |
| 2026-05-06 11:59:45 | status_scrape | rps=0.78  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 11:59:50 | status_scrape | rps=-0.59  err=6.82%  p99=5.0ms  chaos=error |
| 2026-05-06 11:59:56 | status_scrape | rps=0.00  err=6.82%  p99=5.0ms  chaos=error |
| 2026-05-06 12:00:01 | status_scrape | rps=0.59  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:00:06 | status_scrape | rps=0.00  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:00:11 | status_scrape | rps=-0.39  err=6.67%  p99=5.0ms  chaos=error |
| 2026-05-06 12:00:13 | policy_violation | **BLOCKED** by `canary` policy |
| 2026-05-06 12:00:16 | status_scrape | rps=0.00  err=6.67%  p99=5.0ms  chaos=error |
| 2026-05-06 12:00:21 | status_scrape | rps=0.78  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:00:26 | status_scrape | rps=0.00  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:00:31 | status_scrape | rps=0.00  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:00:36 | status_scrape | rps=0.00  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:00:42 | status_scrape | rps=-0.59  err=6.52%  p99=5.0ms  chaos=error |
| 2026-05-06 12:00:47 | status_scrape | rps=0.19  err=6.38%  p99=5.0ms  chaos=error |
| 2026-05-06 12:00:52 | status_scrape | rps=0.39  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:00:57 | status_scrape | rps=0.20  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:01:02 | status_scrape | rps=0.00  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:01:07 | status_scrape | rps=-0.59  err=6.38%  p99=5.0ms  chaos=error |
| 2026-05-06 12:01:12 | status_scrape | rps=0.00  err=6.38%  p99=5.0ms  chaos=error |
| 2026-05-06 12:01:17 | status_scrape | rps=0.78  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:01:22 | status_scrape | rps=-0.59  err=6.25%  p99=5.0ms  chaos=error |
| 2026-05-06 12:01:28 | status_scrape | rps=0.00  err=6.25%  p99=5.0ms  chaos=error |
| 2026-05-06 12:01:33 | status_scrape | rps=0.79  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:01:38 | status_scrape | rps=0.00  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:01:43 | status_scrape | rps=0.00  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:01:48 | status_scrape | rps=-0.59  err=6.12%  p99=5.0ms  chaos=error |
| 2026-05-06 12:01:53 | status_scrape | rps=0.20  err=6.00%  p99=5.0ms  chaos=error |
| 2026-05-06 12:01:58 | status_scrape | rps=0.00  err=6.00%  p99=5.0ms  chaos=error |
| 2026-05-06 12:02:03 | status_scrape | rps=0.20  err=5.88%  p99=5.0ms  chaos=error |
| 2026-05-06 12:02:09 | status_scrape | rps=0.19  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:02:14 | status_scrape | rps=0.00  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:02:19 | status_scrape | rps=-0.20  err=5.88%  p99=5.0ms  chaos=error |
| 2026-05-06 12:02:24 | status_scrape | rps=0.00  err=5.88%  p99=5.0ms  chaos=error |
| 2026-05-06 12:02:29 | status_scrape | rps=0.39  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:02:34 | status_scrape | rps=0.00  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:02:39 | status_scrape | rps=-10.40  err=0.00%  p99=0.0ms  chaos=none |
| 2026-05-06 12:02:42 | promote | Promoted to `stable` |
| 2026-05-06 12:02:44 | status_scrape | rps=0.00  err=0.00%  p99=0.0ms  chaos=none |
| 2026-05-06 12:02:49 | status_scrape | rps=0.20  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:02:54 | status_scrape | rps=0.00  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:03:00 | status_scrape | rps=0.20  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:03:05 | status_scrape | rps=0.00  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:03:10 | status_scrape | rps=0.20  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:03:15 | status_scrape | rps=0.00  err=0.00%  p99=5.0ms  chaos=none |
| 2026-05-06 12:03:20 | status_scrape | rps=-0.39  err=0.00%  p99=5.0ms  chaos=none |

---

## Policy Violations

The following policy violations were recorded:

- `2026-05-06 11:26:11` [infrastructure] Disk free 132.0GB is below minimum 99999.0GB
- `2026-05-06 11:28:07` [infrastructure] Disk free 132.0GB is below minimum 99999.0GB
- `2026-05-06 12:00:13` [canary] Error rate 0.0667 (6.67%) exceeds maximum %!f(int=01)%

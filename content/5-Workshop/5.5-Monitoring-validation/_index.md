---
title: "Monitoring, validation, and troubleshooting"
date: 2026-06-15
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

# 5.5. Monitoring, validation, and troubleshooting

A successful deployment does not prove that every workflow is correct. After the resources are running, I validate three layers: infrastructure, application behavior, and business workflows.

## 1. CloudWatch Logs

The Task Definition uses `awslogs` to send Spring Boot stdout/stderr to a log group such as:

```text
/shopsflow/ecs/backend
```

Important log events include:

- container and Spring Boot startup;
- missing environment variables;
- datasource, migration, or database authentication failures;
- JWT/RBAC exceptions;
- mail or Google OAuth failures when enabled;
- VNPAY URL creation and verification failures;
- HTTP `4xx`/`5xx` responses;
- the deployed revision.

Passwords, tokens, and complete secrets must not be written to logs.

## 2. Metrics to review

| Service | Important metric or status |
|---|---|
| ECS | Running task count, CPU, memory, deployment status, stopped reason |
| ALB | HealthyHostCount, UnHealthyHostCount, TargetResponseTime, HTTP 4xx/5xx |
| RDS | CPU, DatabaseConnections, FreeStorageSpace, FreeableMemory |
| CloudFront | Request count, error rate, cache hit rate |

For a short workshop, alarms should focus on high-impact conditions such as no healthy targets or low RDS storage.

## 3. Infrastructure validation

### Scenario A — Frontend delivery

- Open the CloudFront domain.
- Expected result: the React SPA loads while the S3 bucket remains private.

### Scenario B — API routing

- Call an API from the frontend.
- Expected result: the request passes through CloudFront and the ALB to a healthy Spring Boot target.

### Scenario C — Private workload

- Confirm that the ECS task has no public IP.
- Expected result: the API remains reachable through the ALB and required outbound calls use NAT.

### Scenario D — Database isolation

- Confirm that RDS Publicly accessible is `No` and port `5432` accepts only `ecs-sg`.

### Scenario E — Task replacement

- Stop one service task.
- Expected result: ECS creates a replacement and the ALB routes only to healthy targets.

## 4. Shopsflow business validation

| Feature area | Main validation |
|---|---|
| Authentication | Sign up, email/OTP when enabled, sign in, Google login, sign out, and token expiry |
| Authorization | Customers cannot call Admin APIs; blocked accounts cannot sign in |
| Catalog | Categories, products, stock adjustment, and pagination work correctly |
| Cart/Order | Cart creation, checkout, order status, and shipping methods |
| Inventory | Concurrent requests do not make stock negative; application transactions/locking handle conflicts |
| Payment | Create a VNPAY URL and verify signature/status before updating the order |
| Return/Refund | Customer request, Admin approval, return, and refund confirmation follow the correct order |
| Review/Support | Order reviews, support chat, and conversation closing |
| Notification | Notifications are created for the correct recipient and event only |

## 5. Payment-flow validation

1. The backend obtains amount and order data from server-side records instead of trusting client values.
2. The backend creates payment parameters and a signature.
3. ECS calls the VNPAY sandbox through the outbound route.
4. The browser opens the Payment URL.
5. On return or callback, the backend verifies checksum, transaction reference, amount, and status.
6. The order changes only after successful verification; repeated requests are handled safely.

## 6. Quick troubleshooting table

| Symptom | First place to check | Common cause |
|---|---|---|
| ECS task stops immediately | ECS stopped reason and CloudWatch logs | Incorrect image, missing role, missing environment variable, insufficient memory |
| Task runs but ALB target is unhealthy | Target health, health path, SG | Wrong port, authenticated health endpoint, `ecs-sg` does not accept `alb-sg` |
| API times out when accessing RDS | Backend log, `rds-sg`, subnet | Incorrect endpoint, route, or SG |
| Database authentication fails | Datasource configuration | Incorrect user, password, or database name |
| Blank frontend or asset 403 | S3 objects, OAC, CloudFront origin | Incorrect upload path or OAC/bucket policy |
| Refresh returns 403/404 | CloudFront error response | Missing SPA fallback |
| API still calls localhost | Frontend build configuration | Incorrect build-time environment variable |
| Payment succeeds but order does not change | Backend payment log | Invalid signature/status or incorrect callback configuration |

## 7. Release validation

- Push a new image tag, register a task revision, and update the service.
- Confirm that the new task is healthy before declaring the release successful.
- Confirm the frontend version after S3 synchronization and CloudFront invalidation.
- Record the image tag, task revision, and deployment time for rollback.

## 8. Cost review

Review Billing/Cost Explorer and the resource pages, especially NAT Gateway, ALB, Fargate, RDS, CloudWatch Logs, and data transfer. Use a suitable log-retention period and do not leave the lab running when it is no longer needed.

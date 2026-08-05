---
title: "Resource cleanup"
date: 2026-06-15
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

# 5.6. Resource cleanup

Cleanup is a workshop step, not an optional appendix. NAT Gateway, ALB, Fargate, and RDS may continue generating charges even when no user accesses the application.

I remove resources in the following dependency order to avoid `resource in use` errors.

## 1. Preserve required artifacts

- Record image tags, task-definition revisions, and important configuration.
- Create a final snapshot when database data must be retained.
- Preserve logs required for the report.
- Keep the ECR repository or S3 artifacts when they are still needed for a demo.

## 2. CloudFront and the frontend S3 bucket

1. Disable the CloudFront distribution.
2. Wait until the disabled configuration finishes deploying.
3. Delete the distribution when it is no longer needed.
4. Empty the S3 bucket.
5. Delete the bucket when frontend artifacts do not need to be retained.

## 3. ECS Service and tasks

1. Set desired count to `0` or delete the service.
2. Wait for all Fargate tasks to stop.
3. Confirm that the target group no longer contains service-managed targets.
4. Delete the ECS cluster when no services or tasks remain.

## 4. ALB and target group

1. Delete custom listeners and rules when required.
2. Delete the Application Load Balancer.
3. Delete the target group after the ECS Service no longer references it.

## 5. ECR

- When artifacts are retained, use a lifecycle policy to remove unnecessary old images.
- For complete cleanup, delete images before deleting the repository.

## 6. RDS

1. Delete the RDS instance.
2. Create a final snapshot when data must be retained.
3. Review remaining manual snapshots and automated backups.
4. Delete the DB subnet group after no database uses it.

## 7. CloudWatch and IAM

- Delete log groups, alarms, and dashboards only when their history is no longer required.
- Delete custom task roles and execution roles after ECS stops using them.
- Do not delete shared roles used by another project.

## 8. NAT Gateway and Elastic IP

1. Delete the NAT Gateway.
2. Wait for the `Deleted` state.
3. Release the unused Elastic IP.

NAT Gateways and unreleased Elastic IPs are commonly forgotten after a lab.

## 9. VPC

After ALB, ECS, RDS, and NAT network interfaces are gone:

1. Delete custom route tables.
2. Detach and delete the Internet Gateway.
3. Delete private and public subnets.
4. Delete custom Security Groups.
5. Delete the VPC.

## 10. Final review

- Check every Region used during the workshop, not only the Region currently open in the Console.
- Open Billing/Cost Explorer and look for resources still generating cost.
- Review remaining Elastic IPs, snapshots, log groups, and ECR images.
- When the demo website remains online, document which resources must continue running and what costs require monitoring.

This step reinforces that cloud deployment includes the full resource lifecycle: create, validate, update, observe, and remove resources when they are no longer needed.

---
title: "Blogs Posted"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3. </b> "
---


During our AWS learning process, our team published three technical posts about issues that are easy to miss when following only the happy path. Our team chose these topics because they forced us to think about operations, cost, networking, and security rather than only whether a service was working.

The published article content is kept unchanged. In this report, we focus on what our team learned from each post and how it influenced the Shopsflow architecture.

### [Blog 1 - 3 AWS edge cases that are easy to miss but can cause real incidents](3.1-Blog1/)

This post covers S3 incomplete multipart uploads, IMDSv2 hop limit with Docker on EC2, and Lambda `/tmp` behavior.

For Shopsflow, the S3 lifecycle/storage lesson is directly relevant to frontend artifacts. The IMDSv2 topic became useful as a comparison point: because the final backend runs on Fargate, our team avoids part of the host/instance-metadata complexity that appears when containers depend on EC2 metadata.

### [Blog 2 - Hidden AWS traps that matter in real deployments](3.2-Blog2/)

This post discusses NAT Gateway/S3 data processing, Glacier overhead for small objects, `iam:PassRole`, and EBS volume modification behavior.

The two topics that influenced Shopsflow most were **NAT Gateway cost** and **`iam:PassRole`**. Fargate tasks need outbound connectivity, so NAT is both a network component and a cost driver. ECS roles also made our team more careful about least privilege and who is allowed to pass roles to services.

### [Blog 3 - Hidden AWS techniques: network cost, MTU, limits, and CloudWatch](3.3-Blog3/)

This article looks at Cross-AZ transfer, Path MTU Discovery, DynamoDB On-Demand behavior, and CloudWatch Logs Insights scan cost.

For a multi-AZ Fargate design, Cross-AZ traffic made our team think more carefully about request paths. The CloudWatch section also reminded our team that observability has cost, so log queries should have a clear time range and purpose.

## What the three Blogs changed for our team

Our team started asking a different set of questions when reviewing architecture: where is traffic going, what can create cost, which role is being passed, what evidence do we have when something fails, and which knowledge applies directly to our current design versus a different architecture.

Writing the posts also helped our team test our own understanding. Reading a topic can feel easy; explaining it clearly is much harder and often exposes the parts we still need to study.

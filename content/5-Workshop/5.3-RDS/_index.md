---
title: "Create private RDS PostgreSQL"
date: 2026-06-15
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

# 5.3. Create private RDS PostgreSQL

## 1. Why the database is created before the ECS Service

The backend needs an endpoint, port, database name, and credentials during startup. I therefore create RDS before completing the ECS Service. If the datasource is incorrect, Spring Boot may stop during startup and the ALB will report an unhealthy target.

## 2. Create a DB subnet group

1. Open the Amazon RDS Console.
2. Create a DB subnet group for the Shopsflow VPC.
3. Select the two private subnets in different Availability Zones.
4. Do not use public subnets for the database tier.

A DB subnet group does not grant connectivity by itself; it only defines where RDS may place network interfaces.

## 3. Create RDS PostgreSQL

| Property | Value or principle |
|---|---|
| Engine | PostgreSQL |
| DB identifier | `database-shopsflow` or the environment-specific equivalent |
| Connectivity | Shopsflow VPC and private DB subnet group |
| Public access | `No` |
| Port | `5432` |
| Security Group | `rds-sg` |
| Backup | Enable automated backup appropriate for the lab duration |
| Credentials | Do not store them directly in source code |


![Shopsflow RDS PostgreSQL instance](images/5-Workshop/rds.jpg?featherlight=false)
*Figure 1. The RDS page confirms that the PostgreSQL instance is available. The backend uses its endpoint through private VPC connectivity.*

## 4. Restrict access with the RDS Security Group



![Inbound rules for the RDS Security Group](images/5-Workshop/rds_sg_inbound_rules.jpg?featherlight=false)
*Figure 2. The RDS Security Group allows PostgreSQL TCP `5432` only from the ECS Security Group and does not expose the database directly to the Internet.*

Do not add `PostgreSQL 5432` from `0.0.0.0/0`. Local administration should use a controlled access method instead of leaving the database public.

## 5. Prepare backend configuration

Record the endpoint and supply the following values to the ECS task through environment variables or secrets:

```properties
SPRING_DATASOURCE_URL=jdbc:postgresql://<rds-endpoint>:5432/<database-name>
SPRING_DATASOURCE_USERNAME=<database-user>
SPRING_DATASOURCE_PASSWORD=<database-password>
```

JWT, mail, and VNPAY secrets must not be hard-coded into the image either.

## 6. Database checks

After RDS becomes `Available`:

1. Confirm that Publicly accessible is `No`.
2. Confirm that the DB subnet group contains private subnets.
3. Confirm that `rds-sg` accepts only `ecs-sg`.
4. Record the endpoint, port, and database name.
5. After ECS is running, execute one read API and one write API for end-to-end validation.

A connection timeout usually indicates routing, subnet, or Security Group problems. An authentication failure usually indicates an incorrect username, password, database name, or datasource URL.

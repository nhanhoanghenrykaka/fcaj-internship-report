---
title: "Week 4 Worklog"
date: 2026-07-06
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Week 4 Objectives:

* Learn Amazon RDS PostgreSQL and design Shopsflow data layer.
* Keep the database private and allow only backend connectivity.
* Understand datasource configuration for ECS tasks.
* Review concurrency and credential handling for order/inventory flows.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **RDS study**<br>- DB subnet group, endpoint, storage, backup<br>- Result: Lab RDS plan | 06/07/2026 | 06/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Database network**<br>- Private RDS, SG only from ECS SG<br>- Result: ECS → RDS path finalized | 07/07/2026 | 07/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Backend config**<br>- Datasource URL, credentials, migration<br>- Result: Runtime config understood | 08/07/2026 | 08/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **Data tests**<br>- Category, product, order, inventory<br>- Result: Backend read/write checked | 09/07/2026 | 09/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Concurrency/security**<br>- Optimistic locking and credentials<br>- Result: Database/security checklist | 10/07/2026 | 10/07/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Week 4 Achievements:

* Designed private RDS PostgreSQL connectivity from ECS.
* Learned to separate network, credential/configuration, and application/migration issues.
* Understood why inventory concurrency also belongs to application/database logic.
* Avoided storing DB credentials in source code and kept Secrets Manager/KMS as future work.

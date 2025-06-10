# DynamoDB Single-Table Design – Fuse-Lite

> Last updated: 2025-06-10

### Entity types

| PK prefix | SK pattern                  | Example item        |
| --------- | --------------------------- | ------------------- |
| `CUST#`   | `PROFILE#{customerId}`      | customer profile    |
| `SUB#`    | `#{subscriptionId}`         | subscription record |
| `RENEW#`  | `#{subscriptionId}#yyyy-mm` | monthly renewal log |

### Base table keys

```yaml
PartitionKey: PK # string
SortKey: SK # string
```

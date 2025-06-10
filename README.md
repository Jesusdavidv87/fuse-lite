# fuse-lite
Low-latency serverless subscription API - learning project
A **serverless subscription engine** inspired by Amazon Fuse.

| Stack | Why |
|-------|-----|
| **Java 17 + Spring Boot 3** | Mirrors Fuse’s micro-service stack |
| **AWS SAM & API Gateway + Lambda** | Pay-per-request, sub-100 ms latency |
| **DynamoDB single-table** | Scale to millions of subscribers, <10 µs reads |
| **SQS + Step Functions** | Async renewals & retry logic |
| **GitHub Actions CI/CD** | Test → build → deploy to dev/prod |
* [DynamoDB single-table design](docs/dynamo-design.md)


> Goal: ship a MVP in 8 weeks, document trade-offs (cost, latency), and use it as
> a discussion artefact when interviewing for the Amazon Fuse SDE Role.

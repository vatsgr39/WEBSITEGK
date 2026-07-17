# Architecture

The UI is a responsive Next.js client; FastAPI owns authorization boundaries, validation and OpenAPI; PostgreSQL is authoritative. Domain calculations are side-effect-free services. Requests carry correlation IDs. Important records store model versions, inputs and audit events. Recommended production deployment is CloudFront/ALB → ECS Fargate services → RDS PostgreSQL, with private S3 uploads, Secrets Manager and CloudWatch/OpenTelemetry. No paid infrastructure is provisioned.

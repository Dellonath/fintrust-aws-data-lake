# 🏢 FinTrust AWS Data Lake

1. [🧾 About FinTrust](#-company-overview-fintrust)  
2. [🎯 Objective](#-objective)  
3. [📌 High-Level Business Requirements](#-high-level-business-requirements)  
   - [1. Data Sources](#1-data-sources)  
   - [2. Use Cases](#2-use-cases)  
   - [3. Functional Requirements](#3-functional-requirements)  
   - [4. Non-Functional Requirements](#4-non-functional-requirements)  
4. [📐 Expected Deliverables](#-expected-deliverables)  
   - [1. Architecture Diagram](#1-architecture-diagram)  
   - [2. Storage Layer Design](#2-storage-layer-design)  
   - [3. Ingestion Strategy](#3-ingestion-strategy)  
   - [4. Security & Governance](#4-security--governance)  
   - [5. Data Quality & Observability](#5-data-quality--observability)  
   - [6. Cost Optimization](#6-cost-optimization)  
5. [✅ Challenge](#-challenge)
6. [🚀 Conventional Commits](#-conventional-commits)
7. [📚 References](#-references)

## 🧾 About FinTrust

**FinTrust** is a digital financial services provider operating across the world. It offers products like personal loans, credit card management, and investment advisory through mobile and web platforms. The company handles high data volume from financial transactions, user behavior, and third-party integrations, demanding robust data infrastructure for analytics, compliance, and real-time decision-making.

## 🎯 Objective
Build a scalable, secure, and cost-effective **data lake on AWS** to centralize raw, curated, and analytics-ready data for **Business Intelligence, Machine Learning, and Compliance Reporting**.

## 📌 High-Level Business Requirements

### 1. Data Sources
- **PostgreSQL RDS**  
  Customer and transaction operational data.
- **Kafka (MSK)**  
  Real-time clickstream and mobile app events.
- **External APIs**  
  Credit score agencies, FX rates.
- **CSV/Excel Files**  
  Monthly partner reports (uploaded to S3).

### 2. Use Cases
- **Regulatory Reporting**
  - Daily snapshots
  - 7-year retention
  - Immutability
- **Customer 360 View**
  - For analytics teams.
- **Real-time Fraud Detection**
  - Streaming ingestion and processing.
- **Data Science Sandbox**
  - Credit scoring models.
- **Dashboarding**
  - Amazon QuickSight and Redshift Spectrum.

### 3. Functional Requirements
- Ingest **batch and streaming data**.
- Centralize all data in **S3** with **lakehouse architecture**.
- Support **schema evolution** and **partitioning**.
- Enable **data discovery** via catalog.
- Secure PII and sensitive data.
- Maintain **audit trails** and **data lineage**.

### 4. Non-Functional Requirements
- Scalable to **10 TB/month** of raw data.
- **99.9% availability** for ingestion and queries.
- **Data Update Latency**
  - Streaming: ≤5 seconds
  - Batch: ≤30 minutes post source readiness.
- Use **serverless** whenever possible.
- **Separation of zones**: raw, curated, analytics.
- Fine-grained **access control** per zone and per team.

## 📐 Expected Deliverables

### 1. Architecture Diagram
End-to-end AWS architecture covering:
- Ingestion (DMS, Glue, Kinesis, Lambda)
- Storage (S3 buckets by zone)
- Cataloging (Glue Data Catalog, Lake Formation)
- Processing (Athena, Glue ETL, EMR)
- Consumption (QuickSight, SageMaker, Redshift Spectrum)
- Governance (IAM, KMS, CloudTrail)

### 2. Storage Layer Design
- Directory structure per zone.
- Partitioning strategy (e.g., date, region, product).
- File formats (Parquet, JSON, Avro) — with trade-off analysis.
- Naming conventions and versioning.

### 3. Ingestion Strategy
- Real-time pipelines (Kinesis Data Firehose / Kafka Connect).
- Batch pipelines (Glue ETL, Lambda, Step Functions).

### 4. Security & Governance
- **Encryption**: SSE-KMS.
- **Column-level security**.
- **Data classification and tagging**.
- **Access control matrix** per role/team.

### 5. Data Quality & Observability
- Data validation (nulls, types, ranges).
- Logging and alerting (CloudWatch, SNS).
- Monitoring and retries.

### 6. Cost Optimization
- S3 Lifecycle policies (transition to Glacier).
- Partition pruning in Athena.
- Minimize small files.
- Use spot instances and serverless compute when applicable.

## ✅ Challenge
Design this system including:
- Clear justification of each AWS service.
- Diagrams or pseudocode for pipelines.
- Governance and cost control decisions.
- Evolution plan from MVP to enterprise-scale platform.

## 🚀 Conventional Commits

Use the following commit message types to maintain consistency and clarity in version control:

- **test**: Indicates the creation or modification of test-related code.  
  _Example: Adding unit tests._

- **feat**: Introduces a new feature to the project.  
  _Example: Adding a new service, functionality, or endpoint._

- **refac**: Refactors code without changing business logic or behavior.  
  _Example: Code improvements after a code review._

- **style**: Formatting or style changes that do not affect the system’s functionality.  
  _Example: Adjusting indentation, removing trailing spaces or comments, updating lint rules._

- **fix**: Applies a bug fix that resolves an error or incorrect behavior.  
  _Example: Adding error handling for a function returning unexpected results._

- **chore**: Development-related tasks that don’t affect code logic or tests.  
  _Example: Updating `.gitignore`, configuring eslint, adding Prettier._

- **docs**: Documentation changes only.  
  _Example: Updating API documentation or README._

- **build**: Changes that affect the build system or external dependencies.  
  _Example: Adding/removing NPM packages or modifying Gulp configuration._

- **perf**: Performance improvements.  
  _Example: Replacing `forEach` with `while`, optimizing SQL queries._

- **ci**: CI/CD configuration changes.  
  _Example: Updating CircleCI, Travis, or GitHub Actions workflows._

- **revert**: Reverts a previous commit.  
  _Example: Reverting commit `abc123` that caused an issue._

## 📚 References
- [Build a Real Time Data Streaming System with AWS Kinesis, Lambda Functions and a S3 Bucket](https://www.youtube.com/watch?v=We5Jr4GGLL0)
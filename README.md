# 🏢 FinTrust AWS Data Lake

## 🧾 About the company

**FinTrust** is a digital financial services provider operating across the world. It offers products like personal loans, credit card management, and investment advisory through mobile and web platforms. The company handles high data volume from financial transactions, user behavior, and third-party integrations, demanding robust data infrastructure for analytics, compliance, and real-time decision-making.


## 🎯 Objective
Build a scalable, secure, and cost-effective **data lake on AWS** to centralize raw, curated, and analytics-ready data for **Business Intelligence, Machine Learning, and Compliance Reporting**.

---

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

---

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

---

### 3. Functional Requirements
- Ingest **batch and streaming data**.
- Centralize all data in **S3** with **lakehouse architecture**.
- Support **schema evolution** and **partitioning**.
- Enable **data discovery** via catalog.
- Secure PII and sensitive data.
- Maintain **audit trails** and **data lineage**.

---

### 4. Non-Functional Requirements
- Scalable to **10 TB/month** of raw data.
- **99.9% availability** for ingestion and queries.
- **Data Update Latency**
  - Streaming: ≤5 seconds
  - Batch: ≤30 minutes post source readiness.
- Use **serverless** whenever possible.
- **Separation of zones**: raw, curated, analytics.
- Fine-grained **access control** per zone and per team.

---

## 📐 Expected Deliverables

### 1. Architecture Diagram
End-to-end AWS architecture covering:
- Ingestion (DMS, Glue, Kinesis, Lambda)
- Storage (S3 buckets by zone)
- Cataloging (Glue Data Catalog, Lake Formation)
- Processing (Athena, Glue ETL, EMR)
- Consumption (QuickSight, SageMaker, Redshift Spectrum)
- Governance (IAM, KMS, CloudTrail)

---

### 2. Storage Layer Design
- Directory structure per zone.
- Partitioning strategy (e.g., date, region, product).
- File formats (Parquet, JSON, Avro) — with trade-off analysis.
- Naming conventions and versioning.

---

### 3. Ingestion Strategy
- Real-time pipelines (Kinesis Data Firehose / Kafka Connect).
- Batch pipelines (Glue ETL, Lambda, Step Functions).

---

### 4. Security & Governance
- **Encryption**: SSE-KMS.
- **Column-level security**.
- **Data classification and tagging**.
- **Access control matrix** per role/team.

---

### 5. Data Quality & Observability
- Data validation (nulls, types, ranges).
- Logging and alerting (CloudWatch, SNS).
- Monitoring and retries.

---

### 6. Cost Optimization
- S3 Lifecycle policies (transition to Glacier).
- Partition pruning in Athena.
- Minimize small files.
- Use spot instances and serverless compute when applicable.

---

## ✅ Challenge
Design this system including:
- Clear justification of each AWS service.
- Diagrams or pseudocode for pipelines.
- Governance and cost control decisions.
- Evolution plan from MVP to enterprise-scale platform.
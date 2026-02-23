This project addresses a critical challenge in pharmaceutical logistics: ensuring the thermal integrity of temperature-sensitive medicines and vaccines during storage and transport. By leveraging a serverless AWS Data Pipeline, the system automates the ingestion, transformation, and visualization of IoT sensor data to maintain safety compliance.
<details>
  <summary><b>Click to view detailed Architecture Diagram</b></summary>
  <br>
  <img src="real time IOT monitoring for medical cold chain storage-Page-2.drawio.png" width="100%">
</details>
 System Architecture & Workflow
The pipeline is designed to handle high-velocity data with zero manual intervention:

1. Data Ingestion (The Gateway)
IoT Sensors: Simulated sensors generate continuous temperature readings.

Amazon Kinesis Data Firehose: Acts as the entry point, capturing streaming data and buffering it for processing.

2. Processing & Transformation (The Brain)
AWS Lambda: A Python-based serverless function that performs real-time ETL.

Data Cleaning: The function parses JSON payloads, converts data types (e.g., text to numeric), and prepares it for the database.

3. Storage & Security (The Core)
Amazon DynamoDB: Stores the latest records for instant querying and dashboard updates.

Amazon S3: Serves as a "Data Lake" for long-term archiving and audit compliance.

AWS IAM: Ensures secure communication between services by enforcing "Least Privilege" access policies.

4. Visualization & Analytics (The Output)
Power BI Dashboard: An interactive interface that visualizes temperature trends.

Critical Alerts: Integrated a fixed -15°C threshold line to trigger visual warnings if temperatures fluctuate.

Advanced Filtering: Users can filter by specific Sensor IDs and time ranges using custom DAX formulas.

🛠 Engineering Excellence (DevOps Approach)
Infrastructure as Code (IaC): The entire AWS environment (Lambda, Firehose, DynamoDB, IAM Roles) is provisioned automatically using Terraform, ensuring the system can be destroyed and rebuilt in minutes.

Local Development: Used Docker and LocalStack to simulate AWS services locally, allowing for rapid testing without cloud costs.

 Technical Stack
Cloud: AWS (Kinesis, Lambda, S3, DynamoDB, IAM).

IaC: Terraform.

Simulation: Docker, LocalStack.

Analytics: Power BI, DAX.

Programming: Python (Data Processing), HCL (Infrastructure).

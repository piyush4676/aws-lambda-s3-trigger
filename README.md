# AWS S3 - Lambda Trigger Project

### 🧩 Overview
This project demonstrates an event-driven AWS architecture where uploading an object to an S3 bucket automatically triggers a Lambda function.

### ⚙️ How It Works
1. A Lambda function is created in AWS Lambda.
2. An S3 bucket is configured as the event source (trigger) for the Lambda.
3. When a new file is uploaded to S3, the Lambda function is executed.
4. The Lambda processes the event and logs details in CloudWatch.

### 🛠️ AWS Services Used
- **Amazon S3** – Object storage for file upload.
- **AWS Lambda** – Serverless compute to process events.
- **AWS IAM** – Permissions and access control for S3 → Lambda communication.

### 📈 Outcome
This project demonstrates real-time event automation using AWS Lambda and S3, a common use case in cloud automation pipelines.

### 📂 Files
- `lambda_function.py` – Lambda handler code.
- `architecture.png` – System architecture diagram (optional).

### 🔗 Author
Piyush Kumar

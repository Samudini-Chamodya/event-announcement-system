# 📣 Event Announcement System — AWS Cloud Project

This project is a cloud-based **Event Announcement System** that allows users to create events and notify subscribers via email in real time. It uses AWS services such as **Lambda**, **SNS**, **API Gateway**, and **IAM**.

> ✅ Developed as part of an AWS learning assignment using only the AWS Free Tier.

---

## 📌 Project Features

- 📬 Send email notifications about new events
- ✅ Automatically trigger on API request using AWS Lambda
- 🌐 API Gateway acts as the public entry point
- 🔐 Uses IAM roles for secure access to AWS services
- 📧 SNS (Simple Notification Service) sends emails to subscribers

---

## 🧱 Architecture Overview


- User triggers the event via HTTP request
- Lambda receives event data and publishes a message to SNS
- SNS sends email to all subscribed users

---

## 🛠️ AWS Services Used

| Service         | Purpose                                                  |
|----------------|----------------------------------------------------------|
| **AWS Lambda**  | Backend logic to process event and publish to SNS       |
| **AWS SNS**     | Sends event email to all email subscribers              |
| **AWS API Gateway** | Public HTTP endpoint to trigger Lambda           |
| **IAM Roles**   | Controls Lambda access to other AWS services            |

---

## 🧪 How to Test the System

1. **Create an SNS Topic**
   - Go to the AWS SNS Console
   - Create a topic (e.g., `EventAnnouncements`)
   - Subscribe your email and confirm it

2. **Create the Lambda Function**
   - Use the `lambda_function.py` code 
   - Set up IAM role with `SNS:Publish` permission
   - Replace the SNS Topic ARN in the code

3. **Create an API Gateway**
   - Create a new REST or HTTP API
   - Connect it to your Lambda function

4. **Trigger with Test Payload**
   - Use Postman,or cURL or a test client to send this JSON:

```json
{
  "title": "Tech Conference 2025",
  "date": "2025-05-10",
  "location": "Colombo"
}
```

** Your email (subscribed to SNS) should receive: **
````
📣 New Event Created!

Title: Tech Conference 2025
Date: 2025-05-10
Location: Colombo
````

👨‍💻 Author
Samudini Chamodya

GitHub: @Samudini-Chamodya



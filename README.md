# Deploing serverless BERT NLP model using AWS Lambda, HuggingFace, and Docker
## What is new with AWS Lambda?
Since December 2020, it is possible now package and deploy Lambda functions as container images of up to 10
GB in storage size and 6 vCPUS. This means that large machine learning models can be deployed using serverless
approach that can be scalled in parallel to AWS lambda.
In this repository, we deploy a BERT Question-Answering API in a serverless AWS Lambda environment.
Therefore we use the Transformers library by HuggingFace, the Serverless Framework, AWS Lambda, and Amazon ECR.

## Project architecture
The backend of the project is serverless and it uses the AWS lambda, dynamoDB, API gateway and ECR for container registry .
Lambda function is the inference server which is wrapped in a docker image and is uploaded to the AWS ECR. AWS API gateway
 is used to send POST request payloads to the lambda function. AWS DynamoDB is used to store the data sent to the inference
 server for monitory purposes. Lambda is able to talk to DynamoDB using and IAM role that only allows write requests to the
 database.

![App Screenshot](assets/arch.png)

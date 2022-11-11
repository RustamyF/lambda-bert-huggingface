# Serverless Applications
Serverless architecture is a way to build and run applications and services without managing
 infrastructure. Your application still runs on servers, but all the server management is done by the cloud providers, such
 as AWS, Azure, or GCP.

## What is AWS lambda?
AWS Lambda is a serverless computing service that can run code without worrying about provisioning or
managing servers. You only pay for what you use and are not charged anything if your application is not being
used. It was originally developed to run computationally less expensive workloads, but now, it can also be
used for larger applications. It can scale pretty well and supports up to thousands of concurrent requests.
 A simple hello world lambda application looks as follows:

```python
import json

def lambda_handler(event, context):
    # TODO logic of the function
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```
This function gets input data (in this example, no input is passed to the function) and returns a status code of 200
 with a 'Hello from Lambda' message. Many AWS services can invoke the lambda function. If we want to access it from
 the internet, we need an API gateway to create an API in front of our Lambda function.
### What is new with AWS Lambda?
Since December 2020, it has been possible now package and deploy Lambda functions as container images of up to 10
GB in storage size and six vCPUS. This means that large machine learning models can be deployed using a serverless
approach that can be called in parallel to AWS lambda.
In this repository, we deploy a BERT Question-Answering API in a serverless AWS Lambda environment.
Therefore we use the Transformers library by HuggingFace, the Serverless Framework, AWS Lambda, and Amazon ECR.

## What is the AWS API gateway?
Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor,
 and secure APIs at any scale. APIs are the "front door" for applications to access data, business logic, or
  functionality from your backend services. API gateway for Lambda basically exposes the lambda function to the internet.
  In our machine learning examples, Lambda is the inference server, and the API gateway is where the data is passed to the
  Lambda function. The following figure shows the architecture of how the API gateway will interact with the python function
  that runs in Lambda.

<img src="assets/lambda-api.png" width="600" height="300">

## What is AWS DynamoDB?
Amazon DynamoDB is a fully managed, serverless, NoSQL database designed to run high-performance applications
 at any scale. If we want to save some data during the transaction of data from and to the API gateway, we can use
 DynamoDB. In the case of machine learning examples, we will store the logs on our inference server. The primary information
 that we are interested in is the data that was sent to the ML inference server and the output of the ML model. We can use
 this to monitor and evaluate the performance of the model. The database can be attached to any visualization tool to
 see the real-time performance of the model.

## Project architecture
The project's serverless backend uses AWS lambda, DynamoDB, API gateway, and ECR for container registry.
The Lambda function is the inference server wrapped in a docker image and uploaded to the AWS ECR. AWS API gateway
 sends POST request payloads to the lambda function. AWS DynamoDB is used to store the data sent to the inference
 server for monitory purposes. Lambda can talk to DynamoDB using an IAM role that only allows writing requests to the
 database.

<img src="assets/arch.png" width="700" height="350">

## How to use
The Infrastructure is deployed using [serverless](https://www.serverless.com/framework/docs) library. Serverless is an easy
to use and secure framework to build applications on AWS Lambda and other serverless functions by other cloud providers.
Install serverless using npm if you don't have it already. If you don't have npm in your machine, follow the installation instructions
in [here](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

```shell
npm install -g serverless
```
If you want to start a project from zero, some templates can be used by running ``serverless `` in the terminal and follow the prompts. Here is an example of
the serverless configuration file to deploy a Lambda function with API gateway:

```yaml
service: serverless-bert-lambda-docker

provider:
  name: aws # provider
  region: us-east-1 # aws region
  memorySize: 5120 # optional, in MB, default is 1024
  timeout: 30 # optional, in seconds, default is 6
functions:
  questionanswering:
    image: ${ACOUNT_NUMBER}.dkr.ecr.us-east-1.amazonaws.com/bert-lambda:v1 #ecr url
    events:
      - http:
          path: qa # http path
          method: post # http method
```
The complete serverless.yaml file that includes DynamoDB integration is written in this [file](serverless-bert/serverless.yaml).
To deploy the architecture, just write the following in the same directory as the [serverless.yaml](serverless-bert/serverless.yaml) file.

```shell script
serverless deploy
```

In the following few pages, we will show examples of using serverless architecture to deploy some of the
commonly used NLP tasks. We will use state-of-the-art approaches using the transformers library.

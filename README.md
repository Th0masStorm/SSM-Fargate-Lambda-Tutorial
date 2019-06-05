# SSM-Fargate-Lambda-Tutorial

This is the repo for my article about dynamic parameters with Fargate and Lambda.

This project  contains the following:

1. Sample app based on Flask, which shows the value of parameter from Parameter Store
2. Cloudformation template for 3 stacks, including: Core, Fargate task and Lambda

## Why do you need this repo

Well... Actually you don't. 
However, if you want to reproduce the steps from my Medium article you can use it.

## Prerequisites

I assume you already have AWS account. If not - you'll need one.

You will need the following installed on your computer:
1. AWS CLI
2. Docker

## Run order

Start with deploying the CFN stack:
```bash
aws cloudformation deploy --profile YOUR_PROFILE --region YOUR_REGION --stack-name YOUR_STACK_NAME --template-file Cloudformation.yaml --capabilities CAPABILITY_IAM
```

Check the outputs of your stack. You will need this information in order to properly configure your Lambda function and ECS parameters.
```bash
aws cloudformation describe-stacks --stack-name YOUR_STACK_NAME --profile YOUR_PROFILE --region YOUR_REGION
```

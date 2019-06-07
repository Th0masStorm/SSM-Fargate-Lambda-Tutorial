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
3. jq

## Run order

Start with deploying the core CFN stack:

```bash
aws cloudformation deploy --profile YOUR_PROFILE --region YOUR_REGION --stack-name YOUR_STACK_NAME --template-file Cloudformation/core.yaml --capabilities CAPABILITY_IAM
```

Check the outputs of your stack. You will need this information in order to properly configure your Lambda function and ECS parameters.

```bash
aws cloudformation describe-stacks --stack-name YOUR_STACK_NAME --profile YOUR_PROFILE --region YOUR_REGION
```

Next up: build the Docker app and push it to the ECR

```bash
cd FlaskApp
REPO=$(aws ecr describe-repositories --profile YOUR_PROFILE --region YOUR_REGION --repository-names YOUR_REPO_NAME | jq .repositories[].repositoryUri | sed -e 's/^"//' -e 's/"$//')
docker build -t ${REPO}:v1 .
$(aws ecr get-login --no-include-email --region YOUR_REGION --profile YOUR_PROFILE)
docker push ${REPO}:v1
```

Now when you have your image pushed, you can deploy your service.
Edit your `taskDefitinion.json` specifying proper parameters.
Register task definition and create a service.
```bash
aws ecs register-task-definition --profile YOUR_PROFILE --region YOUR_REGION --cli-input-json file://taskDefinition.json
aws ecs create-service --profile YOUR_PROFILE --region YOUR_REGION \
    --cluster mycluster \
    --launch-type FARGATE \
    --task-definition YOUR_TASK_DEF \
    --desired-count 1 \
    --platform-version LATEST \
    --network-configuration "awsvpcConfiguration={subnets=[YOUR_SUBNETID1, YOUR_SUBNETID2],securityGroups=[YOUR_SG],assignPublicIp=ENABLED}" \
    --service-name app
```

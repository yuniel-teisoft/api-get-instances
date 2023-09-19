# AWS SAM Project - List EC2 Instances

This project is a simple AWS Serverless Application Model (SAM) that lists all running EC2 instances in the AWS account where the SAM is executed. The project is written in Python and uses AWS SAM, AWS Lambda, and AWS API Gateway.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- AWS CLI already configured with Administrator permission
- [Python 3 installed](https://www.python.org/downloads/)
- [Docker installed](https://www.docker.com/community-edition)
- [SAM CLI installed](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

### Installing

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-repo-url
```

Next, navigate to the project's directory:

```bash
cd your-project-directory
```

Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

### Deployment

To deploy the application, you can use the following commands:

```bash
sam build
sam deploy --guided
```

During the prompts:
- Enter a stack name
- Enter your desired AWS Region
- Accept the defaults for the remaining prompts

## Usage

After deployment, you can access the API Gateway endpoint URL to list the running EC2 instances. The URL is in the following format:

```
https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/instances/
```

## Built With

- [AWS SAM](https://aws.amazon.com/serverless/sam/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS API Gateway](https://aws.amazon.com/api-gateway/)
- [Python 3](https://www.python.org/)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## Authors

- Your Name

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

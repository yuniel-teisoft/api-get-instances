import boto3
import json
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.event_handler import Response, content_types
from aws_lambda_powertools.event_handler import APIGatewayRestResolver, CORSConfig

tracer = Tracer()
logger = Logger()
cors_config = CORSConfig(allow_headers=["*"], max_age=300)
app = APIGatewayRestResolver(cors=cors_config)
cors_config = CORSConfig(allow_headers=["*"], max_age=300)
app = APIGatewayRestResolver(cors=cors_config)


@app.get("/instances")
def get_instances_ec2():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    logger.info("conectado...")
    reservations = ec2_client.describe_instances(
        Filters=[
            {
                "Name": "instance-state-name",
                "Values": ["running"],
            }
        ]
    ).get("Reservations")
    logger.info("filtrando...")
    instance_list = []
    try:
        for reservation in reservations:
            logger.info(f"reservation...{reservation}")
            for instance in reservation["Instances"]:
                logger.info("instance...{instance}")
                instance_id = instance["InstanceId"]
                instance_type = instance["InstanceType"]
                public_ip = instance["PublicIpAddress"]
                private_ip = instance["PrivateIpAddress"]
                instance_list.append(
                    {
                        "instanceId": instance_id,
                        "instanceType": instance_type,
                        "publicIp": public_ip,
                        "privateIp": private_ip,
                    }
                )
                logger.info(
                    f"Instancia ->{instance_list}"
                )
    except Exception as e:
        logger.error(str("error", e))
        return Response(
            status_code=500,
            content_type=content_types.APPLICATION_JSON,
            headers={},
            body=json.dumps({"data": str(e), "status": 500}),
        )

    return Response(
        status_code=200,
        content_type=content_types.APPLICATION_JSON,
        headers={},
        body=json.dumps({"data": instance_list}),
    )


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    """

    :param event:p
    :param context:
    :return:
    """
    return app.resolve(event, context)

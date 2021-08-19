import boto3
import os
import logging

logger = logging.getLogger("__name__")
logger.setLevel(os.environ.get("LOG_LEVEL", logging.INFO))
from botocore.exceptions import ClientError

mwaa = boto3.client('mwaa')

# list mwaa environments via boto3
def list_mwaa_environments():
    name = mwaa.list_environments()
    print(name)
    return name

def lambda_handler(event, context):
    logger.info(event)

    try: 
        for mwaa_environment in list_mwaa_environments().get('Environments'):
            return mwaa_environment
    except ClientError as e:
        logger.error(e.response['Error']['Message'])
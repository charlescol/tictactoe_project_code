import json
from lib.controller.business_logic import *

""" lambda entry point for remove a connectionId from db"""
def lambda_handler(event, context):
    remove(event['requestContext']['connectionId'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

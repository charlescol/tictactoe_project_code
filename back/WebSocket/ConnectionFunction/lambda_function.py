import json
from lib.controller.business_logic import *

""" lambda entry point for insert a connectionId"""
def lambda_handler(event, context):
    create(event['requestContext']['connectionId'])
    return {'statusCode': 200,}
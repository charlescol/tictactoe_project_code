import json
import boto3
from lib.controller.business_logic import *

""" lambda entry point for message broadcasting """
def lambda_handler(event, context):
    data = json.loads(event['body'])['data'].split('+')
    
    # get the message type and broadcast in a json format
    if data[0] == 'chat' : 
        broadcastMsg(selectAll(), '{"type":"'+data[0]+'","message":"'+data[1]+'", "psn":"'+data[2]+'"}')
    elif data[0] == 'board' : 
        broadcastMsg(selectAll(), '{"type":"'+data[0]+'","board":"'+data[1]+'", "psn1":"'+data[2]+'", "psn2":"'+data[3]+'" , "player":"'+data[4]+'"}')
    elif data[0] == 'user' :
        broadcastMsg(selectAll(), '{"type":"'+data[0]+'","queue":"'+data[1]+'"}')
        
    return {'statusCode': 200, }

# Broadcast to all client with boto3d, id_list: list of client id, message : message to broadcast
def broadcastMsg(id_list:list, message) :
    client = boto3.client('apigatewaymanagementapi', endpoint_url='https://g78qc0xisd.execute-api.us-east-1.amazonaws.com/production') # get parent gateway instance
    for id in id_list :
        client.post_to_connection(Data=message, ConnectionId=id[0]) # Broadcast to all clients

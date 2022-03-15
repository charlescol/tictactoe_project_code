import boto3
import json

""" Class to interact with the socket functions """
class Hub : 
    client = None # boto3 client
    
    """ Broadcast a string to all clients by calling the lambda  : broadcast function"""
    @staticmethod
    def broadcast_message(message:str) -> None :
        if Hub.client == None :
            Hub.client = boto3.client('lambda') # create the client if not done
        response = Hub.client.invoke(
            FunctionName = 'arn:aws:lambda:us-east-1:778949908015:function:BroadcastMessage', # function arn
            InvocationType = 'RequestResponse',
            Payload = json.dumps({'body' : '{"data":"'+message+'"}'}) # add a body layer to be opened by the function
        )
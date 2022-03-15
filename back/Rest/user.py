import json
from lib.const import *
from lib.models.user import User
from lib.controller.business_logic import *

""" lambda function :  Called when an user needs to be created """
def create_handler(event, context):
    try :
        psn = json.loads(event['body'])['psn'] # get psn from body
        user = User.from_psn(psn) # create local user
        create_user(user) # call controller
        # return created user
        return { 
            "statusCode": 200,
            "body": json.dumps({
                "id": user.id,
                "psn": user.psn,
                "version": user.version,
                "date": user.date
            }),
        }
    except Exception :
        return {"statusCode": 500}

""" lambda function :  Called when an user needs to be deleted """
def delete_handler(event, context):
    try :
        user = User.from_dic(json.loads(event['body'])) # get user from body
        remove_user(user) # call controller
        return {"statusCode": 200,}
    
    except (ValueNotMatchError, UserNotExistsError) :
        return {"statusCode": 410}

    except Exception :
        return {"statusCode": 500}

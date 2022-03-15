import json
import traceback
from  lib.controller.business_logic import *

""" lambda function : Called when a new move is played"""
def playedEvent_handler(event, context) : 
    try :
        _json = json.loads(event['body']) # get body
        user, position = User.from_dic(_json['user']), _json['position'] # get user and move index
        result = playedEvent(user, position) # call controller
        return {"statusCode": 200 }

    except (ValueNotMatchError, UserNotAllowedError) :
        return {"statusCode": 410, 'message': traceback.format_exc() }

    except Exception :
        return {"statusCode": 500, 'message': traceback.format_exc()}

""" lambda function : Called to create a game (only for development)""" 
def create_handler(event, context) :
    try :
        game = create()
        return {
            "statusCode": 200,
            "body": json.dumps({
                "id": game.id,
                "board": str(game.board),
                "p1": str(game.player1),
                "p2": str(game.player2),
                "date" : game.date,
                "version" : game.version
            }),
        }
    except Exception :
        return {"statusCode": 500, 'message': traceback.format_exc()}

import json
import logging
import os
import time
import uuid
import random
import boto3

dynamodb = boto3.resource('dynamodb')

def create(event, context):

    data = json.loads(event['body'])

    if 'value' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
        return

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'name': data['value'][0],
        'id': str(uuid.uuid1()),
        'Logs': [
            {"Id": data['value'][1],
            "start_time": int(time.time()),
            "end_time": int(time.time()) + 5,
            "start_amount": data['value'][2],
            "end_amount": data['value'][3],
            "state": "active"
            },
            {"Id": data['value'][1] + 50000000,
            "start_time": int(time.time()) + 60,
            "end_time": int(time.time()) + 100,
            "start_amount": data['value'][2] + 2222,
            "end_amount": data['value'][3] + 2222,
            "state": "active"
            },
            {"Id": data['value'][1] + 100000000,
            "start_time": int(time.time()) + 500,
            "end_time": int(time.time()) + 600,
            "start_amount": data['value'][2] + 7777777,
            "end_amount": data['value'][3] + 77777777,
            "state": "active"
            }
        ]
        # 'checked': False,
    }
    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }


    return response


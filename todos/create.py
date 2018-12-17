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

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    d = tuple(data['value'])

    item = {
        'name': d[0],
        'id': str(uuid.uuid1()),
        'Logs': [
            {"Id": d[1]},
            {"start_time": int(time.time())},
            {"end_time": int(time.time()) + 5},
            {"start_amount": d[2]},
            {"end_amount": d[3]},
            {"state": "active"}
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


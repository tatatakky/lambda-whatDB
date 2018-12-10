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

    item = {
        'name': data['value'][0],
        'id': str(uuid.uuid1()),
        'data': [
            data['value'][1],
            data['value'][2],
            data['value'][3]
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


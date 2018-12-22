import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'name': event['pathParameters']['name']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "headers": {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Credentials" : True
            },
        "body": json.dumps(result['Item'],cls=decimalencoder.DecimalEncoder)
    }

    return response

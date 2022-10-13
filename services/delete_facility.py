import json
import boto3
import random
from decimal import Decimal

dynamodbTableName = 'BIKO-BETA-FACILITY-TABLE'
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table(dynamodbTableName)


def delete_facility(facility_primary_email_id):
    try:
        response = table.delete_item(
            Key={
                'facility_primary_email_id': facility_primary_email_id
            },
            ReturnValues = 'ALL_OLD'
        )
        body = {
            'Operation': 'DELETE',
            'Message': 'SUCCESS',
            'deletedItem': response
        }
        return build_response(200, body)
    except:
        return build_response(400, "There was an Error") 

def build_response(statusCode, body=None):
    response = {
        "statusCode": statusCode,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Max-Age": 2592000,
            "Access-Control-Allow-Methods": "OPTIONS, POST, GET, DELETE, PATCH",
        }
    }

    if body is not None:
        response["body"] = json.dumps(body, cls=DecimalEncoder)
    print(response)
    return response
    
# CUSTOM SERIALIZER FOR HANDLING DATATYPES
class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)
import json
import boto3
import random
from decimal import Decimal

dynamodbTableName = 'BIKO-BETA-FACILITY-TABLE'
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table(dynamodbTableName)


def get_facilities():
    # Try to scan patients from the database
    try:
        response = table.scan()
        print(response)
        result = response['Items']
        data = random.shuffle(result)
        result = result[:40]

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            result.extend(response['Items'])
            
        return build_response(200, result)
        

    except Exception as e:
        return build_response(400, f'{e}')

    
       

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

get_facilities()
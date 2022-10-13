import json
import boto3
import random
from decimal import Decimal



dynamodbTableName = 'BIKO-BETA-FACILITY-TABLE'
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table(dynamodbTableName)

def get_facility(facility_primary_email_id):

    # try to get the Facility from the database
    try:
        response = table.get_item(
            Key={
                'facility_primary_email_id': facility_primary_email_id
            }
        )
        if 'Item' in response:
            return build_response(200, response['Item'])
        else:
            return build_response(404, 'Item Not Found')

    except:
        return build_response(404, 'Item Not Found')

test_data = 'tochinwachukwu33@gmail.com'



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


get_facility(test_data)
import json
import boto3
import random
import pprint
from decimal import Decimal

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
    pprint(response)
    return response
    
# CUSTOM SERIALIZER FOR HANDLING DATATYPES
class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)
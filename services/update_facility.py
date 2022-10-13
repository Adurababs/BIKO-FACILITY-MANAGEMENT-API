import json
import boto3
import random
import pprint
from decimal import Decimal

dynamodbTableName = 'BIKO-BETA-FACILITY-TABLE'
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table(dynamodbTableName)


def bulk_upload(primary_key, test_dict):
    for key, value in test_dict.items():
        update_facility(primary_key, key, value)
        print("item updated")

def update_facility(facility_primary_email_id, update_key, update_value):
    try:
        response = table.update_item(
            Key={'facility_primary_email_id': facility_primary_email_id},
            UpdateExpression='set %s = :value' % update_key,
            ExpressionAttributeValues={':value': update_value},
            ReturnValues='UPDATED_NEW')
        body = {
            'Operation': 'UPDATE',
            'Message': 'SUCCESS',
            'UpdatedAttributes': response
        }
        return build_response(200, body)

    except:
        return build_response(400, "There was an Error")

test_dict = {
    "facility_primary_email_id": "jidesanya@gmail.com",
    "password": "$2a$10$td0enz6Fzn7Q8mbqTjU0HOase9gMPtnRzxS8OTB/rx0gGwfOvVHnS",
    "facility_name": "UPDATED_JIDE SANYA LEKKI",
    "facility_code": "FACILITY-180250653482-LEKKI PHASE ONE",
    "facility_location": "YABA PHASE ONE",
    "facility_email": "jidesanya@gmail.com",
    "facility_bank_name": "ZENITH BANK",
    "facility_account_number": "2150295684",
    "facility_account_name": "NWACHUKWU TOCHUKWU CHARLES",
    "facility_admin_name": "UPDATED_MARY SLESSOR",
    "facility_admin_phone_number": "08172573305",
    "facility_admin_email_address": "maryslessor@gmail.com",
    "admin_house_address": "25B ADEBAYO DOHERTY LEKKI PHASE 1",
    "facility_logo": "https://www.pngitem.com/pimgs/m/515-5154167_transparent-background-hospital-icon-hd-png-download.png",
    "is_user_online": True,
    "date_facility_registered": "2022-10-13"
}



def build_response(statusCode, body=None):
    response = {
        "statusCode": statusCode,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Max-Age": 2592000,
            "Access-Control-Allow-Methods":
            "OPTIONS, POST, GET, DELETE, PATCH",
        }
    }

    if body is not None:
        response["body"] = json.dumps(body, cls=DecimalEncoder)
    # print(response)
    return response


# CUSTOM SERIALIZER FOR HANDLING DATATYPES
class DecimalEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

bulk_upload("jidesanya@gmail.com", test_dict)

import json
import boto3
import random
import utils.build_response as build_response
from decimal import Decimal
from services import get_facilities
from services import get_facility
from services import delete_facility
import services.update_facility as update_facility
import services.search_facility as search_facility

dynamodbTableName = 'BIKO-BETA-FACILITY-TABLE'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(dynamodbTableName)


# Here I define the methods

get_method = 'GET'
post_method = 'POST'
patch_method = 'PATCH'
delete_method = 'DELETE'

# Here I define the paths

facility_path = '/facility'
facilities_path = '/facilities'
health_path = '/health'
search_path = '/search'


def lambda_handler(event, context):
    # TODO implement
    # Here I get the path and the method from the event payload
    httpMethod = event['httpMethod']
    path = event['path']
    print(httpMethod, path)
    


# Here I define my route functions
    if httpMethod == get_method and path == health_path:
        response = build_response(200)
    elif httpMethod == get_method and path == facility_path:
        response = get_facility(event['queryStringParameters']['facility_primary_email_id'])
    elif httpMethod == get_method and path == facilities_path:
        response = get_facilities()
    elif httpMethod == patch_method and path == facility_path:
        request_body = json.loads(event['body'])
        response = update_facility(
            request_body['facility_primary_email_id'], request_body['update_key'], request_body['update_value'])
    elif httpMethod == delete_method and path == facility_path:
        request_body = json.loads(event['body'])
        response = delete_facility(request_body['facility_primary_email_id'])
    else:
        response = build_response(404, 'Not Found')
    return response

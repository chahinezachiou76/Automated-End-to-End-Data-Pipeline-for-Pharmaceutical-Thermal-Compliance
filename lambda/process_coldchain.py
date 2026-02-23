import boto3
import json

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4566', region_name='us-east-1')
table = dynamodb.Table('VaccineAlerts')

def lambda_handler(event, context):
    s3 = boto3.client('s3', endpoint_url='http://localhost:4566')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    for line in content.splitlines():
        data = json.loads(line)
        temp = data.get('temperature')
        if temp > -18:
            table.put_item(Item={
                'BatchID': data['shipment_id'],
                'Timestamp': data['timestamp'],
                'Temperature': str(temp),
                'Status': 'CRITICAL'
            })
    return {'status': 'Success'}

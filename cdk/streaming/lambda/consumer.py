import json, boto3, os, datetime, base64
s3 = boto3.client('s3')

def handler(event, context):
    print(event)
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])

        now = datetime.datetime.now().strftime('%d%m%Y%H%M%S')
        s3.put_object(
            Bucket=os.environ['RAW_BUCKET'],
            Key=f'output_{now}.json',
            Body=payload,
            ContentType="application/json"
        )
    return {'statusCode': 200, 'event': event}

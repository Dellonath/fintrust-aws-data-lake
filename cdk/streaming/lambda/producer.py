import boto3, json

data = {
    "transaction_id": "c6a3f972-1b8e-4d6f-8f0a-9dbb6e30a521",
    "timestamp": "2025-08-09T21:45:00Z",
    "customer": {
        "customer_id": "cust-1001",
        "name": "John Doe",
        "email": "john.doe@example.com",
        "country": "BR"
    },
    "account": {
        "account_id": "acc-987654",
        "type": "savings",
        "balance": 12500.75
    },
    "transaction": {
        "amount": 250.00,
        "currency": "USD",
        "type": "deposit",
        "status": "completed",
        "channel": "mobile_app"
    },
    "metadata": {
        "source_system": "FinTrustApp",
        "processing_time_ms": 85
    }
}

def handler(event, context):
    client = boto3.client('kinesis')
    client.put_record(
        StreamName='finstrust-data-stream',
        Data=json.dumps(data),
        PartitionKey=data['transaction_id']
    )
    return {'statusCode': 200, 'event': json.dumps(event), 'data': json.dumps(data)}

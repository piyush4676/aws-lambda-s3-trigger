import json

def lambda_handler(event, context):
    # TODO implement
    print('hello')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Piyush!')
    }

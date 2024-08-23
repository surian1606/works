#use aws profile
import boto3
session = boto3.Session(profile_name='admin')

#create a dynamodb table with low-level client
client = session.client('dynamodb')
client.create_table(
    TableName='employees',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

#dynamodb table waiter to wait until table is created
client.get_waiter('table_exists').wait(TableName='employees')

#printout the number of items in the table
response = client.describe_table(TableName='employees')
#print(response['Table']['ItemCount'])
print (response)
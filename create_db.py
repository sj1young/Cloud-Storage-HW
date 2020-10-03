import boto3

dyndb = boto3.resource('dynamodb', region_name = 'us-east-2', aws_access_key_id = 'AKIA4QBUGQUKMD4LPNUA',aws_secret_access_key = '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')

try:
    table = dyndb.create_table(
    TableName='DataTable',
        KeySchema=[
        {
        'AttributeName': 'PartitionKey',
        'KeyType': 'HASH'
        },
        {
        'AttributeName': 'RowKey',
        'KeyType': 'RANGE'
        }
        ],
    AttributeDefinitions=[
        {
        'AttributeName': 'PartitionKey',
        'AttributeType': 'S'
        },
        {
        'AttributeName': 'RowKey',
        'AttributeType': 'S'
        },
        ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
        }
    )
except:
    #if there is an exception, the table may already exist. if so...
    table = dyndb.Table("DataTable")
    print("exception or table existed")
    
table.meta.client.get_waiter('table_exists').wait(TableName='DataTable')
print(table.item_count)

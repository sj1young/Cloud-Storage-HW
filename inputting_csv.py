import boto3
import csv
s3 = boto3.resource('s3', aws_access_key_id = 'AKIA4QBUGQUKMD4LPNUA',aws_secret_access_key = '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')

dyndb = boto3.resource('dynamodb', region_name = 'us-east-2', aws_access_key_id = 'AKIA4QBUGQUKMD4LPNUA',aws_secret_access_key = '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')
table = dyndb.Table("DataTable")
with open('experiments.csv', 'r') as csvfile:
    csvf = csv.reader(csvfile, delimiter=',', quotechar='|')
    for item in csvf:
        print(item)
        body = open('datafiles/'+item[3], 'rb')
        s3.Object('sjy16-hw-bucket', item[3]).put(Body=body )
        md = s3.Object('sjy16-hw-bucket', item[3]).Acl().put(ACL='public-read')
        url = " https://s3-us-east-2.amazonaws.com/sjy16-hw-bucket/"+item[3]
        metadata_item = {'PartitionKey': item[0], 'RowKey': item[1],
            'description' : item[4], 'date' : item[2], 'url':url}
        table.put_item(Item=metadata_item)
        
response = table.get_item(
    Key={'PartitionKey': 'exp4',
         'RowKey': '4'})
item = response['Item']
print(item)
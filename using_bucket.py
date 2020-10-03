import boto3

s3 = boto3.resource('s3', aws_access_key_id = 'AKIA4QBUGQUKMD4LPNUA',aws_secret_access_key = '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')
bucket = s3.Bucket("sjy16-hw-bucket")

pic = open('db.jpg','rb')
o = s3.Object('sjy16-hw-bucket','test').put(Body=pic)
s3.Object('sjy16-hw-bucket', 'test').Acl().put(ACL='public-read')
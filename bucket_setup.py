import boto3

s3 = boto3.resource('s3', aws_access_key_id = 'AKIA4QBUGQUKMD4LPNUA',aws_secret_access_key = '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')
s3.create_bucket(Bucket='datacont-name', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
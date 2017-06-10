import boto3

from django.conf import settings


class S3Upload:
    
    def __init__(self):
        # Get the service client
        self.s3 = boto3.client('s3')
        self.bucket = settings.AWS_STORAGE_BUCKET_NAME

    def upload_file(self, file)
        # Upload tmp.txt to bucket-name at key-name
        s3.upload_file("tmp.txt", "bucket-name", "key-name")
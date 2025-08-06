import os
import boto3 # when workignwith local env and want to connect with aws 
from dotenv import load_dotenv
load_dotenv()

class s3Client:
    s3_client = None
    s3_resource = None
    def __init__(self , region_name = os.environ['AWS_DEFAULT_REGION']):
        if s3Client.s3_resource is None or s3Client.s3_client is None:
            __access_key_id = os.environ["AWS_ACCESS_KEY_ID"]
            __secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]

            if __access_key_id is None:
                raise Exception("Environment  Variable :AWS_ACCESS_KEY_ID  is not set")
            if __secret_access_key is None:
                raise Exception("Environment  Variable :AWS_SECRET_ACCESS_KEY  is not set")
            s3Client.s3_resource = boto3.resource("s3",
                                                aws_access_key_id =__access_key_id,
                                                aws_secret_key = __secret_access_key,
                                                region_name = region_name)
            s3Client.s3_client = boto3.client("s3",
                                                aws_access_key_id =__access_key_id,
                                                aws_secret_key = __secret_access_key,
                                                region_name = region_name)
            self.s3_resource  = s3Client.s3_resource
            self.s3_client = s3Client.s3_client
import logging
import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
	try:
		if region is None:
			s3_client = boto3.client('s3')
			s3_client.create_bucket(
				Bucket = input("Enter the bucket name:").strip()
				)
		else:
			s3_client= boto3.client('s3',region_name=region)
				if len(bucket_name) == 0:
					print("Bucket name can not be Blank!!")
				else:
					s3_client.create_bucket(
					Bucket=input("Enter the bucket name:").strip(),
					CreateBucketConfiguration={
					'LocationConstraint':'us-west-2',
				},
			)
	except ClientError as e:
		logging.error(e)
		return False

	return True
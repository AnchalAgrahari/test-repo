import boto3
client = boto3.client('s3')
response = client.create_bucket(
    Bucket=input("Enter the unique bucket name:").strip(), 
        CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2',
    },
)
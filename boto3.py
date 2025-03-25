import  boto3
client = boto3.client('s3')



if __name__ == '__main__':
    try:
        response = client.create_bucket(
        bucket_name = input("Enter the bucket name: ").strip(),
        CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2',
    },
)
        if len(bucket_name) != 0:
            print("Bucket name must be unique: ",bucket_name)
        else:
            print("Bucket connot be created")




 

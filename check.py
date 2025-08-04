import boto3
from botocore.exceptions import NoCredentialsError

session = boto3.Session()
credentials = session.get_credentials()
print("Access Key:", credentials.access_key)
print("Secret Key:", credentials.secret_key)
print("Token:", credentials.token)
#

import boto3
from botocore.exceptions import NoCredentialsError
import glob



for bucket in s3.buckets.all():
    print(bucket.name)

client = boto3.client('s3')

    # Call to S3 to retrieve the policy for the given bucket
result = client.get_bucket_acl(Bucket='bucket')
print(result)

import logging
from botocore.exceptions import ClientError

# Defining a function to upload files to AWS

files = glob.glob('pathname', recursive=False)
def upload_to_aws(local_file, bucket, s3_file):
    for file in files:
        s3 = boto3.client('s3')

        try:
            s3.upload_file(local_file, bucket, s3_file)
            print("Upload Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False


uploaded = upload_to_aws('local_file', 'bucket_name', 's3_file_name')

# To do the Bonus part of the quest, I wanted to convert the file to a CSV so that I could run a SQL query on it
#Reading text into CSV

import pandas as pd

data_current = pd.read_csv('data_current.txt', delimiter = '\t')


# adding column headings
data_current.columns = ['series_id', 'year', 'period', 'value','footnote_codes']

# store dataframe into csv file
data_current.to_csv('data_current.csv',
                index = None)


# To remove the trailing space from all the columns

data_current.columns = data_current.columns.str.strip()

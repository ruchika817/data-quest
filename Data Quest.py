#!/usr/bin/env python
# coding: utf-8

# In[5]:


### DATA QUEST
# Importing modules

import boto3
from botocore.exceptions import NoCredentialsError
import glob


# In[9]:


# Defining a function to upload files to AWS


ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXX'
SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

files = glob.glob('pathname', recursive=False)



def upload_to_aws(local_file, bucket, s3_file):
    for file in files:
        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

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


# In[6]:


# To do the Bonus part of the quest, I wanted to convert the file to a CSV so that I could run a SQL query on it
#Reading text into CSV

import pandas as pd

data_current = pd.read_csv('data_current.txt', delimiter = '\t')

  
# adding column headings 
data_current.columns = ['series_id', 'year', 'period', 'value','footnote_codes'] 
  
# store dataframe into csv file 
data_current.to_csv('data_current.csv',  
                index = None) 


# In[7]:


data_current


# In[ ]:





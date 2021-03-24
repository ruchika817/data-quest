## Data-quest
### 1. Here is the link to the uploaded files on AWS S3

https://s3.console.aws.amazon.com/s3/buckets/bucket322?region=us-east-1&tab=objects

I have now changed the permissions for the files. To do it in code, I would add extra arguments in the upload function to have ACL as 'public-read'. I have done that in my code file above.

### 2. I have a python file as well as a jupyter notebooks file with the script for uploading files onto AWS in this bucket.
I have now written the python file on Atom and it should run in any python program. If you are running it in terminal, 
python3 data_quest.py
should be able to run it

### 3. The functions that I have defined do not have hard coded names of the files. Those are the arguments. Can you please elaborate on what you mean by your question?

### 4. To avoid using the user Access_key and Secret_key in the code, one could create a credentials file in your aws folder in your terminal. Once that is made, there is default profile created which can be used by Boto3 to interact with the AWS account. 

### 5.To fix the space, I used pandas 
data_current.columns = data_current.columns.str.strip()
### This removes all white spaces in all columns

### 6. For the BONUS question, I converted the text file to a CSV using pandas ( code is in the python file) so that it could be loaded to Athena. I then created a table in Athena and loaded the csv. I have included a screenshot below and the Query ID. 

### Here is the screenshot of the table that I created in Athena

![Screen Shot 2021-03-23 at 10 16 29 PM](https://user-images.githubusercontent.com/13152268/112244277-70dad400-8c25-11eb-98f3-a3e9d56750a5.png)

The Query ID is c376ab01-c294-450e-ad4e-15cc5f6333e7

I am including the CSV of the result in my files above. For some reason, it did not read any of the data. I am not sure why. I know it has something to do with the path. I will think about it. 

### The SQL code would simply be
### SELECT * from Table 
### WHERE value = 2.6






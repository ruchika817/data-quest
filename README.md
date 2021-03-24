## Data-quest
### 1. Here is the link to the uploaded files on AWS S3

https://s3.console.aws.amazon.com/s3/buckets/bucket322?region=us-east-1&tab=objects

I have now changed the permissions for the files. To do it in code, I would add extra arguments in the upload function to have ACL as 'public-read'. 

### 2. I have a python file as well as a jupyter notebooks file with the script for uploading files onto AWS in this bucket.
I have now written the python file on Atom and it should run in any python program. If you are running it in terminal, 
python3 data_quest.py
should be able to run it

### 3. The functions that I have defined do not have hard coded names of the files. Those are the arguments. I am not sure what you mean by that question.

For the BONUS question, I converted the text file to a CSV using pandas ( code is in the python file) so that it could be loaded to Athena. But for some reason, it kept giving me file empty. The file was definitely a table as seen in notebook. But Athena was not reading the data and I was not able to figure out why. I think I will keep working on that to figure it out. 

### The SQL code would simply be
### SELECT * from Table 
### WHERE value = 2.6

### Here is the screenshot of the table that I created in Athena

![Screen Shot 2021-03-23 at 10 16 29 PM](https://user-images.githubusercontent.com/13152268/112244277-70dad400-8c25-11eb-98f3-a3e9d56750a5.png)

The Query ID is c376ab01-c294-450e-ad4e-15cc5f6333e7
I am included the CSV of the result. For some reason, it did not read any of the data. I am not sure why. I know it has something to do with the path. I will think about it. 





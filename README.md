## Data-quest
### Here is the link to the uploaded files on AWS S3

https://s3.console.aws.amazon.com/s3/buckets/bucket322?region=us-east-1&tab=objects

## I have a python file as well as a jupyter notebooks file with the script for uploading files onto AWS in his folder

''' For the BONUS question, I converted the text file to a CSV ( code is in the python file) so that it could be loaded to Athena. But for some reason, it kept giving me file empty. I think I was doing it right. Also, Athena did read it right once and then when I ran it again, the data was not there. 

The SQL code would simply be
SELECT * from athenatest 
WHERE value = 2.6


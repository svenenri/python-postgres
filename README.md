# python-postgres
Serverless project using psycopg2 in a Lambda coded in Python

Note: Ensure Docker is running on your local machine for this specific project.
Note: sls and serverless can be used interchangeably on the cli. 

Deploy an entire project: sls deploy 
(https://serverless.com/framework/docs/providers/aws/cli-reference/deploy/)

Update the function only (handler.py file): sls deploy function -f hello 
(https://serverless.com/framework/docs/providers/aws/cli-reference/deploy-function/)

Remove the Lambda from AWS environment: sls remove 
(https://serverless.com/framework/docs/providers/aws/cli-reference/remove/)

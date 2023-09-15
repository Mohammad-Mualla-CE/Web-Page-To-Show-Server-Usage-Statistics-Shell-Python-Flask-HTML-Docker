# Server-Usage-Statistics

## Flask Application that provides API’s to monitor the server’s status
The main objective of this application is to return usage statistics of the server to the user to be
used for monitoring purposes over a defined period of time.

## How to run the applicatio:
1-Make a directory in your server machine : mkdir /application   
2-Change the location to directory /application : cd /application   
3-Copy the file docker-compose.yml to the directory /application/   
4-Run the command : docker-compose up  

## Details

# ● The Application will provide disk,memory, and cpu usage statistics for each hour over the last
24 hours by default
# ● Provide a GET API to return CPU usage statistics for the each hour in the last 24 hours
and one to provide current usage
# ● Provide a GET API to return disk usage statistics for the each hour in the last 24 hours
and one to provide current usage
● Provide a GET API to return memory usage statistics for the each hour in the last 24
hours and one to provide current usage
● Enable logging and log all actions(API calls, function calls.etc)
● Wrapper functions to log the actions
● Unit tests for the functions
● The statistics saved in a database
● The statistics will collected using a crontab started when the application container starts
● Containerize the application and provide docker file
● Push the docker image to docker hub with tag v1
● Use containerized image for database
● Run the application and database containers on two different machines
● Database details(credentials,ip,port,..etc) should be passed to the application container
using env variables


  

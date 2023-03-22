# AWS

- S3 https://s3.console.aws.amazon.com/s3/buckets?region=eu-west-1
- EC2 https://eu-west-1.console.aws.amazon.com/ec2/home?region=eu-west-1#Instances:instanceState=running
- ECR https://eu-west-1.console.aws.amazon.com/ecr/repositories/public/632496433960/lat_ecr?region=eu-west-1








# EC2 

## get project
sudo yum install git -y

git clone https://github.com/rikard-helgegren/LAT_AWS.git

## build it 

sudo yum install docker -y
sudo docker build -t api .

## run it

sudo docker run -v $(pwd)/src/:/app/ -p 8080:8080 --name api api

## access it 
web : http://54.216.239.102:8080/markets \
Terminal : curl http://54.216.239.102:8080/markets



# Call with boddy

curl -X POST -H "Content-type: application/json" -d "{\"Country\" : \"sweden\", \"leverage\" : \"1\"}" "localhost:8080/post_json"


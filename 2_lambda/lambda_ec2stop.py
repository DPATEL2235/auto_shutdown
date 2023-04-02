import boto3
region = 'us-east-2'
instances = ['i-01d1dbdaf5b588681', 'i-03c4bc473dbb353a2']  #'i-01d1dbdaf5b588681', 'i-03c4bc473dbb353a2' are instance id
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
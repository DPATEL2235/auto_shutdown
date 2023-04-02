Before creating the Lambda function we have to assign the role to that function which has an authority to do the changes in the configuration of the EC2 instance. Below are the steps for that.

Step 1: In our case we have to create one policy which has permission for start and stop the instance.(Screenshot lambda_policy)

Step 2: Create the role which has the policy which we have created before.(Scrrenshot : lambda_role)

Step 3: Creating the lambda function which will stop the instance when it has been triggered by Amazon EventBridge.
        FOr the lambda function we are using the python and for the role we are assigning the role which we have created just before.
        Code for that (lambda_ec2stop.py)

Step 4: Last step for the implemetation is to trigger this lambda function in particular time period when we want to off the machine.


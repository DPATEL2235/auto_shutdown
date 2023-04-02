In eventbridge we are going to use rules for triggering the lambda function.  Here rule match the incoming events and sends to the target for the processing.

Step 1: first of all in rule detail section we need to apply schedule as rule type because using the cron expression we are going to shutdown the instance on time.

Step 2: Then appling the cron expression which we want to have, here we want to shutdown the instance in everyweeknd of the month.so according to that I have applied the cron (scrrenshot eventbridge_cron)

Step 3: Then we need to select the target for that, so here we have target service as lambda and the name of the function. then updatinfg the rule it has been created

step 4: flow between lambda function and eventbridge is shown in (Screenshot: eventbridge_flow)
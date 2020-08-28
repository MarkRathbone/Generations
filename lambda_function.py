import boto3
import os

s3 = boto3.client('s3')
sns = boto3.client('sns')
topicArn = os.envrion['topicArn']

def lambda_handler(event, context):
    data = s3.get_object(Bucket='thisismysillylambdabucket', Key='kubermatic.txt')
    text = data['Body'].read().decode('utf-8')
    topic_arn = topicArn
    message = 'The word count in the file kubermatic.txt is: ' + str(len(text.split()))
    sns.publish(TopicArn=topic_arn,Message=message)
    return(message + ' <-- This message has been sent to subscribers.')

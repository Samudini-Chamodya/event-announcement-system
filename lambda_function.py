import json
import boto3

sns = boto3.client('sns')
TOPIC_ARN = "arn:aws:sns:us-east-1:314146315247:EventAnnouncements"  

def lambda_handler(event, context):
    body = json.loads(event['body'])
    title = body.get('title')
    date = body.get('date')
    location = body.get('location')

    message = f"📣 New Event Created!\nTitle: {title}\nDate: {date}\nLocation: {location}"
    
    # Publish to SNS
    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=message,
        Subject="New Event Notification"
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Event created and announcement sent!'})
    }
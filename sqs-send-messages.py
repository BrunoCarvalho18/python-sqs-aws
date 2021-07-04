import boto3

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='teste')

# Criar uma nova mensagem
resposta  = queue.send_message(MessageBody='boto3', MessageAttributes={
    'Author': {
        'StringValue': 'Bruno',
        'DataType': 'String'
    }
})
# A resposta não é um recurso, mas vamos receber o id da mensagem
print(resposta.get('MessageId'))
print(resposta.get('MD5OfMessageBody'))
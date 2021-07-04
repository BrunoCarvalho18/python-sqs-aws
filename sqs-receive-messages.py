import boto3

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='teste')

for mensagem in queue.receive_messages(MessageAttributeNames=['Author']):
    autor_texto = ''
    if mensagem.message_attributes is not None:
         autor_nome = mensagem.message_attributes.get('Author').get('StringValue')
         if  autor_nome:
             autor_texto = ' ({0})'.format(autor_nome)

    # Print out the body and author (if set)
    print('Hello, {0}!{1}'.format(mensagem.body,  autor_texto))
from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print('Mensagem não enviada: {}'.format(err))
    else:
        print('Mensagem enviada para o tópico [{}]'.format(msg.topic()))

conf = {
    'bootstrap.servers': 'localhost:9092',  
    'client.id': 'python-producer'
}

producer = Producer(conf)

topic = 'GABRIEL'  


for i in range(10):
    message = 'Mensagem de exemplo {}'.format(i)
    producer.produce(topic, key=str(i), value=message, callback=delivery_report)


producer.flush()

from confluent_kafka import Consumer, KafkaError

conf = {
    'bootstrap.servers': 'localhost:9092',  
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)

topic = 'GABRIEL' 
consumer.subscribe([topic])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('Fim da partição, pulando para a próxima.')
        else:
            print('Erro no consumo: {}'.format(msg.error()))
    else:
        print('Recebido mensagem: key [{}], value [{}]'.format(msg.key(), msg.value()))

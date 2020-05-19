from kafka import TopicPartition
from kafka import KafkaConsumer

topic = 'test1'
partition = 0
tp = TopicPartition(topic,partition)
server_addresses = ['192.168.0.5:9092']

kafkaConsumer = KafkaConsumer(group_id="a", auto_offset_reset='earliest', 
        bootstrap_servers=server_addresses, enable_auto_commit=True, auto_commit_interval_ms=1000)
kafkaConsumer.assign([tp])

for msg in kafkaConsumer:
    print(msg.value)

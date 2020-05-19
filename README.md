# python-read-kafka-partitions
Consume from special kafka partitions

Ther is two python file. Each of them, consume message from one partition of "test1" kafka topic.


step1- create kafka topic "test1" with 2 partitions:
./bin/kafka-topics.sh --create --bootstrap-server 192.168.0.5:9092 --topic test1 --partitions 2

step2- send some message to "test1" topic:
./bin/kafka-console-producer.sh --topic test1 --broker-list 192.168.0.5:9092
>hi1
>hi2
>hi3
>hi4
>hi5     
>hi6
>hi7
>hi8

step3- run consume_partition_0 python file, to read message from partition 0:
python consume_partition_0.py 
b'hi1'
b'hi3'
b'hi5'
b'hi7'


step4- run consume_partition_1 python file, to read message from partition 1:
python consume_partition_1.py 
b'hi1'
b'hi3'
b'hi5'
b'hi7'

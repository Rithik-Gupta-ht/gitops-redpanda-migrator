from confluent_kafka.admin import AdminClient
from confluent_kafka import Consumer , TopicPartition

conf = {
    'bootstrap.servers': 'pkc-921jm.us-east-2.aws.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': 'OJK5IVIBKAYA7FIP',
    'sasl.password': 'Qtm4EKcJyco5bbevDWN6xxcpkZ+WKYFcDK1+GHQNcX7yDQmv25pbk0/e0HCKwsmO',
    'group.id': 'group-test',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False
}

# Get topic partitions
topic = "test_topic"
consumer = Consumer(conf)

# Get metadata
md = consumer.list_topics(timeout=10)

# Validate topic exists
if topic not in md.topics:
    print(f"❌ Topic '{topic}' not found in metadata.")
    exit(1)

# Get partition IDs
partitions = md.topics[topic].partitions
partition_ids = partitions.keys()  # Should be a list of integers

# Convert to TopicPartition
topic_partitions = [TopicPartition(topic, pid) for pid in partition_ids]

# Get committed offsets
offsets = consumer.committed(topic_partitions, timeout=10)

# Print
for tp in offsets:
    print(f"Partition: {tp.partition}, Committed Offset: {tp.offset}")
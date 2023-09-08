import os
from confluent_kafka import Producer, Consumer
from dotenv import load_dotenv

load_dotenv()

# Kafka configuration
kafka_config = {
    # Use Django settings for broker address
    'bootstrap.servers': os.getenv("KAFKA_SERVER"),
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'SCRAM-SHA-512',
    # Use Django settings for username
    'sasl.username': os.getenv("KAFKA_USER"),
    # Use Django settings for password
    'sasl.password': os.getenv("KAFKA_PASSWORD"),
    # Set your desired group ID here
    'group.id': ' bkpzcrni-real-time-email-consuming',
    'auto.offset.reset': 'earliest',
}

# Create a Kafka producer or consumer with the configuration
producer = Producer(kafka_config)
consumer = Consumer(kafka_config)

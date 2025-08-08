import os
from dotenv import load_dotenv

# ENV_FILE = os.getenv("ENV_TYPE", ".env.redpanda")
# load_dotenv(ENV_FILE)

BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "localhost:9092")
TOPIC = os.getenv("TOPIC", "test-topic")
GROUP_ID = os.getenv("GROUP_ID", "test-group")

# Auth
SECURITY_PROTOCOL = os.getenv("SECURITY_PROTOCOL", "SASL_SSL")
SASL_MECHANISM = os.getenv("SASL_MECHANISM", "PLAIN")
SASL_USERNAME = os.getenv("KAFKA_USERNAME")
SASL_PASSWORD = os.getenv("KAFKA_PASSWORD")

COMMON_CONF = {
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'security.protocol': SECURITY_PROTOCOL,
    'sasl.mechanism': SASL_MECHANISM,
    'sasl.username': SASL_USERNAME,
    'sasl.password': SASL_PASSWORD,
}

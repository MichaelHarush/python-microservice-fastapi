from kafka import KafkaProducer
from app.core.config import settings

producer = KafkaProducer(bootstrap_servers=f'{settings.KAFKA_HOST}')



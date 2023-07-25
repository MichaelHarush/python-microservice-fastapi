import base64

from app.core.config import settings
from app.queue.producer import producer


def send_one(message_json_str:str):
    producer.send(f"{settings.KAFKA_TOPIC}", message_json_str.encode())

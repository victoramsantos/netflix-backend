import json
import os

from kafka import KafkaProducer

from src.library.logger.Logger import Logger


class SupportRepository:
    def __init__(self):
        self.__producer = KafkaProducer(
            bootstrap_servers=[os.getenv("KAFKA_SERVER")],
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        self.__drink_topic = os.getenv("KAFKA_TOPIC_SUPPORT")

    def call_support(self, user_id: int, message: str):
        Logger.info(f"publishing to {self.__drink_topic}: {user_id}")
        self.__producer.send(
            topic=self.__drink_topic,
            value={
                "userId": user_id,
                "message": message
            }
        )
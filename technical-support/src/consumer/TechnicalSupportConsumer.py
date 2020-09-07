import json
import os

from kafka import KafkaConsumer

from src.library.logger.Logger import Logger


class TechnicalSupportConsumer:
    def __init__(self):
        self.__topic = KafkaConsumer(
            os.getenv("KAFKA_TOPIC_SUPPORT"),
            bootstrap_servers=[os.getenv("KAFKA_SERVER")]
        )

    def consumes(self):
        for message in self.__topic:
            order_attender = json.loads(message.value.decode('utf-8'))
            self.attend(order_attender)

    def attend(self, order):
        Logger.info(f"Attending user_id={order['userId']} message={order['message']}")

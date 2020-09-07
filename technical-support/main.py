import configparser
import os

from src.library.logger.Logger import Logger

if __name__ == "__main__":
    configuration = configparser.ConfigParser()
    configuration.read("./application.ini")

    environment: str = os.getenv("ENVIRONMENT", "DEV")
    Logger.info(f"Running with environment: {environment}")

    for key, value in configuration[environment].items():
        if not os.getenv(key.upper(), None):
            os.environ[key.upper()] = str(value)

    from src.consumer.TechnicalSupportConsumer import TechnicalSupportConsumer

    technical_support_consumer = TechnicalSupportConsumer()
    technical_support_consumer.consumes()

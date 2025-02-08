from .yandex_export import YandexExporter
import logging

logging.basicConfig(filename="logs.txt", level=logging.INFO, format="%(asctime)s - %(message)s")
logging.info("Exporter is ready...")
print("Exporter is ready...")
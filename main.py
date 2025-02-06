import os
from yandex_exporter import YandexExporter
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    TOKEN = os.getenv("YANDEX_MUSIC_TOKEN")
    exp = YandexExporter(TOKEN)
    exp.load_csv()


if __name__ == "__main__":
    main()

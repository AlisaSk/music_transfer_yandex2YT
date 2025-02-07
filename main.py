import os
from yandex_exporter import YandexExporter
from youtube_importer import YouTubeImporter
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    YANDEX_TOKEN = os.getenv("YANDEX_MUSIC_TOKEN")
    YT_CLIENT_ID = os.getenv("YOUTUBE_CLIENT_ID")
    YT_CLIENT_SECRET = os.getenv("YOUTUBE_CLIENT_SECRET")
    exporter = YandexExporter(YANDEX_TOKEN)
    importer = YouTubeImporter(YT_CLIENT_ID, YT_CLIENT_SECRET)
    #exporter.load_csv()
    importer.create_playlist_from_csv()


if __name__ == "__main__":
    main()

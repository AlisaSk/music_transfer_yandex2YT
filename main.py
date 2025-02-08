import os
from yandex_exporter import YandexExporter
from youtube_importer import YouTubeImporter
from dotenv import load_dotenv
import argparse

def get_args():
    parser = argparse.ArgumentParser(
        prog="Music transfer yandex2YT",
        description="The program transfer music from Yandex Music to YouTube Music",
        epilog="If you have any questions left, please contact me via https://github.com/AlisaSk"
    )
    parser.add_argument("-n", "--playlist_name",type=str,required=True, help="Name of a playlist you want to create")
    parser.add_argument("-d", "--playlist_desc", type=str, required=True, help="Description of a playlist you want to create")
    parser.add_argument("-f", "--output_file", type=str, required=False, default="songs", help="Output file with artists and songs names (default: songs.csv)")
    parser.add_argument("-N", "--songs_number", type=int, required=True, help="Number of songs you want to add (latest N songs will be added)")
    return  parser.parse_args()

def main() -> None:
    args = get_args() 
    file_name = args.output_file + ".csv"
    print(file_name)
    load_dotenv()
    YANDEX_TOKEN = os.getenv("YANDEX_MUSIC_TOKEN")
    YT_CLIENT_ID = os.getenv("YOUTUBE_CLIENT_ID")
    YT_CLIENT_SECRET = os.getenv("YOUTUBE_CLIENT_SECRET")
    exporter = YandexExporter(YANDEX_TOKEN, file_name, args.songs_number)
    importer = YouTubeImporter(YT_CLIENT_ID, YT_CLIENT_SECRET, args.playlist_name, args.playlist_desc, file_name)
    exporter.load_csv()
    importer.create_playlist_from_csv()


if __name__ == "__main__":
    main()

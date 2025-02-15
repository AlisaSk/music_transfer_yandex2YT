from yandex_music import Client
import pandas as pd
import os
import logging

logging.basicConfig(filename="logs.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

class YandexExporter:
    def __init__(self, output_file:str, songs_number:int) -> None:
        self.client = Client(os.getenv("YANDEX_MUSIC_TOKEN")).init()
        self.file_name = output_file
        self.songs_number = songs_number
        self.data = []


    def extract_data(self) -> None:
        tracks = self.client.users_likes_tracks().tracks
        info_counter = 0
        for i in range(self.songs_number):
            track = tracks[i]
            track = track.fetch_track()
            artist = track.artists_name()[0]
            name = track.title
            self.data.append([artist, name])
            info_counter += 1
            if (info_counter % 5 == 0):
                logging.info(f"Extracted {info_counter} tracks...")
                print(f"Extracted {info_counter} tracks...")

    def load_csv(self) -> None:
        self.extract_data()
        df = pd.DataFrame(self.data, columns=["Artist", "Song"])
        df.to_csv(self.file_name, index=False)
        logging.info(f"Data has been saved to {self.file_name}")
        print(f"Data has been saved to {self.file_name}")

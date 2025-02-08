from yandex_music import Client, Artist
import pandas as pd

class YandexExporter:
    def __init__(self, token:str, output_file:str, songs_number:int) -> None:
        self.client = Client(token).init()
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
            if (info_counter % 25 == 0):
                print(f"Extracted {info_counter} tracks...")

    def load_csv(self) -> None:
        self.extract_data()
        df = pd.DataFrame(self.data, columns=["Artist", "Song"])
        df.to_csv(self.file_name, index=False)
        print(f"Data has been saved to {self.file_name}")

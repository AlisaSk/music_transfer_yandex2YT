from yandex_music import Client, Artist
import pandas as pd


class YandexExporter:
    def __init__(self, token:str) -> None:
        self.client = Client(token).init()
        self.data = []


    def extract_data(self) -> None:
        tracks = self.client.users_likes_tracks().tracks
        info_counter = 0
        for i in range(100):
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
        df.to_csv("yandex_music.csv", index=False)
        print("Data has been saved to yandex_music.csv")

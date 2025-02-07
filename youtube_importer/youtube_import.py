import pandas as pd
from ytmusicapi import YTMusic, OAuthCredentials    


class YouTubeImporter:
    def __init__(self, client_id:str, client_secret:str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.data = pd.read_csv("yandex_music.csv")
        # print(self.data.head())
        self.ytmusic = YTMusic('oauth.json', oauth_credentials=OAuthCredentials(client_id=self.client_id, client_secret=self.client_secret))

    def create_playlist_from_csv(self) -> None:
        print("test")
        #print(ytmusic.get_charts())
        songs = self.collect_songs_ids()
        playlist_id = self.ytmusic.create_playlist("TEST 10 SONGS", description="please work", video_ids=songs)
        print(f"Playlist {playlist_id} created")

    def collect_songs_ids(self) -> list:
        songs_ids = []
        for row in self.data.itertuples(index=False):
            search_str = str(row[1]) + " " + str(row[0]) # row[1] -- song, row[0] -- artist
            print(search_str)
            search_res = self.ytmusic.search(query=search_str, limit=1)
            top_result_id = [item["videoId"] for item in search_res if item["category"] == "Top result"]
            print(top_result_id[0])
            songs_ids.append(top_result_id[0])
        return songs_ids
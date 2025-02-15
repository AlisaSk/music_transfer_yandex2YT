import os
import pandas as pd
from ytmusicapi import YTMusic, OAuthCredentials    
import logging

logging.basicConfig(filename="logs.txt", level=logging.INFO, format="%(asctime)s - %(message)s")



class YouTubeImporter:
    def __init__(self, playlist_name:str, playlist_desc:str, file_name:str) -> None:
        self.playlist_name = playlist_name
        self.playlist_desc = playlist_desc
        self.file_name = file_name
        self.ytmusic = YTMusic('oauth.json', oauth_credentials=OAuthCredentials(client_id=os.getenv("YOUTUBE_CLIENT_ID"), client_secret=os.getenv("YOUTUBE_CLIENT_SECRET")))

    def create_playlist_from_csv(self) -> None:
        # pass SONGS as param
        songs = self.collect_songs_ids()
        playlist_id = self.ytmusic.create_playlist(title=self.playlist_name, description=self.playlist_desc, video_ids=songs)
        logging.info(f"Playlist {self.playlist_name} is created (id: {playlist_id})")
        print(f"Playlist {self.playlist_name} (id: {playlist_id}) created")

    def collect_songs_ids(self) -> list:
        songs_ids = []
        data = pd.read_csv(self.file_name)
        logging.info("Collecting Yandex song's ids...")
        print("Collecting Yandex song's ids...")
        for row in data.itertuples(index=False):
            search_str = str(row[1]) + " " + str(row[0]) # row[1] -- song, row[0] -- artist
            search_res = self.ytmusic.search(query=search_str, limit=1)
            top_result_id = [item["videoId"] for item in search_res if item["category"] == "Top result"]
            songs_ids.append(top_result_id[0])
        logging.info("... Collecting is completed")
        print("...Completed")
        return songs_ids
    
    
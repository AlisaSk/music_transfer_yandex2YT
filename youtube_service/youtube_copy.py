import os
from ytmusicapi import YTMusic, OAuthCredentials    
import logging

logging.basicConfig(filename="logs.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

class YouTubeCopy:
    def __init__(self, playlist_id:str, songs_n: int) -> None:
        self.playlist_id = playlist_id
        self.songs_n = songs_n
        self.ytmusic = YTMusic('oauth.json', oauth_credentials=OAuthCredentials(client_id=os.getenv("YOUTUBE_CLIENT_ID"), client_secret=os.getenv("YOUTUBE_CLIENT_SECRET")))

    def collect_ytsongs_ids(self) -> list:
        all_liked_songs = self.ytmusic.get_liked_songs()
        logging.info(f"Total liked songs collected {len(all_liked_songs["tracks"])}")
        limited_tracks = all_liked_songs['tracks'][:self.songs_n]   
        logging.info(f"{self.songs_n} liked songs are collected for adding")
        video_ids = [track['videoId'] for track in limited_tracks]
        return video_ids

    def add_songs_to_playlist(self) -> None:
        songs_ids = self.collect_ytsongs_ids()
        self.ytmusic.add_playlist_items(playlistId=self.playlist_id, videoIds=songs_ids, duplicates=True)
        logging.info(f"{self.songs_n} liked songs are added to playlist with ID: {self.playlist_id}")

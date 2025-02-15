import tkinter as tk
from tkinter import messagebox
from UI.view.log_youtube_view import LogYoutubeView
from UI.view.colors import Colors


class YoutubeParamsView:
    def __init__(self, root:tk.Tk):
        self.root = root
        for widget in root.winfo_children():
            widget.destroy()
        self.set_scene()

    def set_scene(self):
        frame = tk.Frame(self.root, bg=Colors.BACKGROUND.value)
        frame.pack(expand=True)

        tk.Label(frame, text="Playlist ID:", fg="black", bg=Colors.BACKGROUND.value).pack(pady=2)
        self.playlist_id = tk.Entry(frame, width=30)
        self.playlist_id.pack(pady=2)

        tk.Label(frame, text="Songs number:", fg="black", bg=Colors.BACKGROUND.value).pack(pady=2)
        self.songs_number = tk.Entry(frame, width=30)
        self.songs_number.pack(pady=2)

        tk.Button(frame, text="Start", command=self.start_transfer, bg=Colors.BUTTON.value, fg="white").pack(pady=10)

    def start_transfer(self):
        id = self.playlist_id.get()
        try:
            songs_n = int(self.songs_number.get())
            LogYoutubeView(self.root, id, songs_n)
        except ValueError as e:
            messagebox.showerror("Music transfer yandex2YT Error", str(e))
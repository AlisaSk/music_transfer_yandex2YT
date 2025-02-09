import tkinter as tk
from tkinter import messagebox
from UI.view.log_page_view import LogPageView
from UI.view.colors import Colors


class YandexParamsView:
    def __init__(self, root: tk.Tk):
        self.root = root
        for widget in root.winfo_children():
            widget.destroy()
        self.set_scene()

    def set_scene(self):
        frame = tk.Frame(self.root, bg=Colors.BACKGROUND.value)
        frame.pack(expand=True)

        tk.Label(frame, text="Playlist name:", fg="black", bg=Colors.BACKGROUND.value).pack(pady=2)
        self.playlist_name = tk.Entry(frame, width=30)
        self.playlist_name.pack(pady=2)

        tk.Label(frame, text="Playlist description:", fg="black", bg=Colors.BACKGROUND.value).pack(pady=2)
        self.playlist_desc = tk.Entry(frame, width=30)
        self.playlist_desc.pack(pady=2)

        tk.Label(frame, text="Name of file for saving songs:", fg="black", bg=Colors.BACKGROUND.value).pack(pady=2)
        self.output_file = tk.Entry(frame, width=30)
        self.output_file.insert(0, "songs.csv")
        self.output_file.pack(pady=2)

        tk.Label(frame, text="Songs number:", fg="black", bg=Colors.BACKGROUND.value).pack(pady=2)
        self.songs_number = tk.Entry(frame, width=30)
        self.songs_number.pack(pady=2)

        tk.Button(frame, text="Start", command=self.start_transfer, bg=Colors.BUTTON.value, fg="white").pack(pady=10)

    def start_transfer(self):
        name = self.playlist_name.get()
        desc = self.playlist_desc.get()
        file = self.output_file.get()
        try:
            if not file.endswith(".csv"):
                raise ValueError("The file name must end with .csv")
            
            songs_n = int(self.songs_number.get())

            LogPageView(self.root, name, desc, file, songs_n)
        except ValueError as e:
            messagebox.showerror("Music transfer yandex2YT Error", str(e))
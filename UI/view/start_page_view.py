import tkinter as tk
from tkinter import messagebox
from UI.view.log_page_view import LogPageView
from dotenv import load_dotenv


class StartPageView:
    def __init__(self, root:tk.Tk):
        self.root = root
        load_dotenv()
        self.root.title("Music Transfer Yandex2YT")
        self.root.geometry("400x300")
        self.root.configure(bg="#282c34")
        self.set_page()
        
    def set_page(self):
        frame = tk.Frame(self.root, bg="#282c34")
        frame.pack(expand=True)

        tk.Label(frame, text="Playlist name:", fg="white", bg="#282c34").pack(pady=2)
        self.playlist_name = tk.Entry(frame, width=30)
        self.playlist_name.pack(pady=2)

        tk.Label(frame, text="Playlist description:", fg="white", bg="#282c34").pack(pady=2)
        self.playlist_desc = tk.Entry(frame, width=30)
        self.playlist_desc.pack(pady=2)

        tk.Label(frame, text="Name of file for saving songs:", fg="white", bg="#282c34").pack(pady=2)
        self.output_file = tk.Entry(frame, width=30)
        self.output_file.insert(0, "songs")
        self.output_file.pack(pady=2)

        tk.Label(frame, text="Songs number:", fg="white", bg="#282c34").pack(pady=2)
        self.songs_number = tk.Entry(frame, width=30)
        self.songs_number.pack(pady=2)

        tk.Button(frame, text="Start", command=self.start_transfer, bg="#61afef", fg="white").pack(pady=10)

    def start_transfer(self):
        name = self.playlist_name.get()
        desc = self.playlist_desc.get()
        file = self.output_file.get() + ".csv"
        try:
            songs_n = int(self.songs_number.get())
            #messagebox.showinfo("Data is correct!", f"Creating playlist: {name}\n: Desc {desc}\nFile: {file}\nN songs: {songs_n}")
            # Здесь можно вызывать свою логику переноса музыки
            LogPageView(self.root, name, desc, file, songs_n)
        except ValueError:
            messagebox.showerror("Music transfer yandex2YT Error", "Number of songs should be an integer!")
        
        # exporter = YandexExporter(file_name, args.songs_number)
        # importer = YouTubeImporter(args.playlist_name, args.playlist_desc, file_name)
        # exporter.load_csv()
        # importer.create_playlist_from_csv()


if __name__ == "__main__":
    root = tk.Tk()
    app = StartPageView(root)
    root.mainloop()
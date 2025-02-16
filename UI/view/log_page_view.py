import tkinter as tk
from tkinter import scrolledtext
import sys
import os
from UI.view.colors import Colors

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from yandex_service import YandexExporter
from youtube_service import YouTubeImporter
import threading


class LogPageView:
    def __init__(self, root:tk.Tk, name:str, desc:str, file:str, songs_n:int):
        self.root = root
        self.name = name
        self.desc = desc
        self.file = file
        self.songs_n = songs_n
        for widget in root.winfo_children():
            widget.destroy()
        self.set_scene()
    
        self.root.after(3000, self.start_app)
        
    def set_scene(self):
        frame = tk.Frame(self.root, bg=Colors.BACKGROUND.value)
        frame.pack(expand=True)

        tk.Label(frame, text="Creating your playlist", fg="black", font=("Arial", 12, "bold"), bg=Colors.BACKGROUND.value).pack(pady=5)
        self.log_display = scrolledtext.ScrolledText(frame, width=50, height=15, bg=Colors.LOG_BG.value, fg="black", font=("Arial", 10), wrap=tk.WORD)
        self.log_display.pack(padx=10, pady=5)
    
        

    def update_logs(self):
        if os.path.exists("logs.txt"):
            with open("logs.txt", "r") as log_file:
                logs = log_file.readlines()

            current_position = self.log_display.yview()

            self.log_display.delete(1.0, tk.END)
            for log in logs:
                self.log_display.insert(tk.END, log)

            self.log_display.yview_moveto(current_position[0])

        self.root.after(1000, self.update_logs)

    def start_app(self):
        exporter = YandexExporter(self.file, self.songs_n)
        importer = YouTubeImporter(self.name, self.desc, self.file)

        self.root.after(0, self.update_logs)

        threading.Thread(target=self.run_transfer, args=(exporter,importer)).start()
       

    def run_transfer(self, exporter, importer):
        exporter.load_csv()
        importer.create_playlist_from_csv()

   


        
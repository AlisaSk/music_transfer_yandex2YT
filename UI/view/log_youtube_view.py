import tkinter as tk
from tkinter import scrolledtext
import sys
import os
from UI.view.colors import Colors

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from youtube_service import YouTubeCopy
import threading


class LogYoutubeView:
    def __init__(self, root:tk.Tk, id:str, songs_n:int):
        self.root = root
        self.id = id
        self.songs_n = songs_n
        for widget in root.winfo_children():
            widget.destroy()
        self.set_scene()
        self.root.after(3000, self.start_app)

    def set_scene(self):
        frame = tk.Frame(self.root, bg=Colors.BACKGROUND.value)
        frame.pack(expand=True)

        tk.Label(frame, text="Adding to your playlist", fg="black", font=("Arial", 12, "bold"), bg=Colors.BACKGROUND.value).pack(pady=5)
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
        editor = YouTubeCopy(self.id, self.songs_n)
        self.root.after(0, self.update_logs)

        threading.Thread(target=self.run_adding, args=(editor,)).start()
        

    def run_adding(self, editor):
        editor.add_songs_to_playlist()
import tkinter as tk
from tkinter import scrolledtext
import sys
import os
import time

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
        #self.start_app()
        self.root.after(5000, self.start_app)
        
    def set_scene(self):
        frame = tk.Frame(self.root, bg="#282c34")
        frame.pack(expand=True)

        tk.Label(frame, text="Creating your playlist", fg="white", font=("Arial", 12, "bold"), bg="#282c34").pack(pady=5)
        self.log_display = scrolledtext.ScrolledText(frame, width=50, height=15, bg="#2e3238", fg="white", font=("Arial", 10), wrap=tk.WORD)
        self.log_display.pack(padx=10, pady=5)
        print("lol")
        

    def update_logs(self):
        """Функция для автоматической подгрузки логов"""
        if os.path.exists("logs.txt"):
            with open("logs.txt", "r") as log_file:
                logs = log_file.readlines()
            
            # Очищаем текущий вывод и добавляем новые строки
            self.log_display.delete(1.0, tk.END)
            for log in logs:
                self.log_display.insert(tk.END, log)

        # Через 1 секунду снова проверяем обновления в логах
        self.root.after(1000, self.update_logs)

    def start_app(self):
        exporter = YandexExporter(self.file, self.songs_n)
        importer = YouTubeImporter(self.name, self.desc, self.file)

        self.root.after(0, self.update_logs)

        threading.Thread(target=self.run_exporter, args=(exporter,)).start()
        threading.Thread(target=self.run_importer, args=(importer,)).start()

        # self.root.after(0, self.run_exporter, exporter)
        # self.root.after(0, self.run_importer, importer)

    def run_exporter(self, exporter):
        """Запуск экспортера и обновление логов"""
        exporter.load_csv()
        # self.update_logs()

    def run_importer(self, importer):
        """Запуск импортера и обновление логов"""
        importer.create_playlist_from_csv()
        # self.update_logs()

        
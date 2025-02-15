import tkinter as tk
from UI.view.yandex_params_view import YandexParamsView
from UI.view.youtube_params_view import YoutubeParamsView
from UI.view.colors import Colors

class StartPageView:
    def __init__(self, root:tk.Tk):
        self.root = root
        self.root.title("Music Transfer Yandex2YT")
        self.root.geometry("400x300")
        self.root.configure(bg=Colors.BACKGROUND.value)
        self.set_page()
        
    def set_page(self):
        frame = tk.Frame(self.root, bg=Colors.BACKGROUND.value)
        frame.pack(expand=True, padx=20, pady=20)


        self.option_var = tk.StringVar(value="yandex")  

        radio_button1 = tk.Radiobutton(frame, text="Transfer from Yandex", variable=self.option_var, value="yandex", fg="black", bg=Colors.BACKGROUND.value)
        radio_button1.pack(pady=2)

        radio_button2 = tk.Radiobutton(frame, text="Transfer from YouTube", variable=self.option_var, value="YT", fg="black", bg=Colors.BACKGROUND.value)
        radio_button2.pack(pady=2)

        tk.Button(frame, text="Continue", command=self.switch_page, bg=Colors.BUTTON.value, fg="white").pack(pady=10)

    def switch_page(self):
        if self.option_var.get() == "yandex":
            YandexParamsView(self.root)
        
        else :
            YoutubeParamsView(self.root)



from dotenv import load_dotenv
import os
import tkinter as tk
from UI.view.start_page_view import StartPageView

def main() -> None:
    if os.path.exists("logs.txt"):
        open("logs.txt", "w").close()  # clean logs.txt
    load_dotenv()
    root = tk.Tk()
    app = StartPageView(root)
    root.mainloop()


if __name__ == "__main__":
    main()

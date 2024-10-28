from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
import yt_dlp as ydl
from tkinter import filedialog

WINDOW_TITLE = "Astol-dlp"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
URL_LABEL = "Video URL                  "
FORMAT_LABEL = "Choose format           "
DOWNLOAD_LABEL = "Download location    "
DOWNLOAD_BUTTON = "Download"
STATUS_LABEL = "Status:"
PROGRAM_TITLE = ">Astoldlp"
BROWSE_BUTTON = "📁 Select Folder"

FORMATS = [
    "mp4",
    "webm"
]

OPTIONS = {
    "format": "best",
    "outtmpl": "%(title)s.%(ext)s",
    "noplaylist": True,
    "progress_hooks": None,
}

def download_video():
    url = url_entry.get()
    download_location = download_entry.get()
    format = dropdown_field.get()
    if not url:
        status_label.config(text="Status: Invalid URL")
        return
    OPTIONS["format"] = format
    if format != "mp4":
        OPTIONS["format"] = "b*[ext=webm]"    

    def progress_hook(d):
        if d["status"] == "finished":
            status_label.config(text=f"Status: Downloaded {d['filename']}")
    OPTIONS["progress_hooks"] = [progress_hook]
    ydlp = ydl.YoutubeDL(OPTIONS)
    try:
        status_label.config(text="Status: Downloading...")
        ydlp.download([url])
    except Exception as e:
        status_label.config(text=f"Status: Error - {e}")

def browse_folder():
    directory = filedialog.askdirectory()
    download_entry.insert(0, directory) 

window = ttk.Window(themename="vapor")
window.title(WINDOW_TITLE)
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.resizable(False, False)
window.iconbitmap("favicon.ico")

bg = PhotoImage(file="img2.png")
canvas = Canvas(window, width=200, height=200)

url_frame = ttk.Frame(window)
url_label = ttk.Label(url_frame, text=URL_LABEL)
url_entry = ttk.Entry(url_frame)
url_label.pack(side=tk.LEFT)
url_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)

download_frame = ttk.Frame(window)
download_label = ttk.Label(download_frame, text=DOWNLOAD_LABEL)
download_entry = ttk.Entry(download_frame)
download_label.pack(side=tk.LEFT)
download_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)

download_button_frame = ttk.Frame(window)
download_button = ttk.Button(download_button_frame, text=DOWNLOAD_BUTTON, command=download_video)
download_button.pack(fill=tk.X, expand=True)

status_frame = ttk.Frame(window)
status_label = ttk.Label(status_frame, text=STATUS_LABEL)
status_label.pack()

program_title_frame = ttk.Frame(window)
program_label = ttk.Label(program_title_frame, text=PROGRAM_TITLE, font=("Josefin Sans",50))
program_label.pack()

browse_button_frame = ttk.Frame(window)
browse_label = ttk.Label(browse_button_frame, text="                                   ")
browse_button = ttk.Button(browse_button_frame, text=BROWSE_BUTTON, command=browse_folder)
browse_label.pack(side=tk.LEFT)
browse_button.pack(side=tk.RIGHT, fill=tk.X, expand=True)

dropdown_frame = ttk.Frame(window)
dropdown_label = ttk.Label(dropdown_frame, text=FORMAT_LABEL)
dropdown_field = ttk.Combobox(dropdown_frame, state="readonly", values=FORMATS)
dropdown_field.set("mp4")
dropdown_label.pack(side=tk.LEFT)
dropdown_field.pack(side=tk.RIGHT, fill=tk.X, expand=True)


program_title_frame.pack(fill=tk.X, padx=20, pady=30)
url_frame.pack(fill=tk.X, padx=100, pady=0)
dropdown_frame.pack(padx=100, pady=30, fill=tk.X, expand=True)
download_frame.pack(fill=tk.X, padx=100, pady=0)
browse_button_frame.pack(fill=tk.X, padx=100, pady=0)
download_button_frame.pack(padx=100, pady=50, fill=tk.X, expand=True)
status_frame.pack(padx=10, pady=0)
canvas.pack(fill=tk.X, expand=True)
canvas.create_image(200, 0, image=bg, anchor="nw")

window.mainloop()

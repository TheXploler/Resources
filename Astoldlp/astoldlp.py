from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
import yt_dlp as ydl

WINDOW_TITLE = "Astol-dlp"
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
URL_LABEL = "Enter video URL:"
FORMAT_LABEL = "Choose format:"
DOWNLOAD_LABEL = "Download location:"
DOWNLOAD_BUTTON = "Download"
STATUS_LABEL = "Status:"

FORMATS = [
    ("Best", "best"),
    ("MP4", "mp4"),
    ("MP3", "mp3"),
    ("WEBM", "webm"),
    ("OGG", "ogg"),
]

OPTIONS = {
    "format": "best",
    "outtmpl": "%(title)s.%(ext)s",
    "noplaylist": True,
    "progress_hooks": None,
}

def download_video():
    url = url_entry.get()
    if not url:
        status_label.config(text="Status: Invalid URL")
        return
    format = format_var.get()
    OPTIONS["format"] = format
    download_location = download_entry.get()
    if download_location:
        OPTIONS["outtmpl"] = download_location + "/" + OPTIONS["outtmpl"]
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

window = ttk.Window(themename="vapor")
window.title(WINDOW_TITLE)
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.resizable(False, False)
window.iconbitmap("favicon.ico")

bg = PhotoImage(file="img2.png")
canvas = Canvas(window, width=600, height=160)

url_frame = ttk.Frame(window)
url_label = ttk.Label(url_frame, text=URL_LABEL)
url_entry = ttk.Entry(url_frame)
url_label.pack(side=tk.LEFT)
url_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)

format_frame = ttk.Frame(window)
format_label = ttk.Label(format_frame, text=FORMAT_LABEL)
format_var = ttk.StringVar()
format_var.set(FORMATS[0][1])
format_buttons = []
for text, value in FORMATS:
    format_button = ttk.Radiobutton(format_frame, text=text, value=value, variable=format_var)
    format_buttons.append(format_button)
format_label.pack(side=tk.LEFT)
for format_button in format_buttons:
    format_button.pack(side=tk.LEFT)

download_frame = ttk.Frame(window)
download_label = ttk.Label(download_frame, text=DOWNLOAD_LABEL)
download_entry = ttk.Entry(download_frame)
download_label.pack(side=tk.LEFT)
download_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)

button_frame = ttk.Frame(window)
download_button = ttk.Button(button_frame, text=DOWNLOAD_BUTTON, command=download_video)
download_button.pack()

status_frame = ttk.Frame(window)
status_label = ttk.Label(status_frame, text=STATUS_LABEL)
status_label.pack()

url_frame.pack(fill=tk.X, padx=10, pady=10)
format_frame.pack(fill=tk.X, padx=10, pady=10)
download_frame.pack(fill=tk.X, padx=10, pady=10)
button_frame.pack(padx=10, pady=10)
status_frame.pack(padx=10, pady=10)
canvas.pack(fill=tk.X)
canvas.create_image(0, 0, image=bg, anchor="nw")

window.mainloop()

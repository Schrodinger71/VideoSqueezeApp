import customtkinter as ctk
from src.ui import VideoCompressorUI
from src.utils import check_ffmpeg
import sys
from tkinter import messagebox

def run_app():
    if not check_ffmpeg():
        messagebox.showerror("FFmpeg не найден", "Установите FFmpeg и добавьте его в PATH.")
        sys.exit(1)

    root = ctk.CTk()
    app = VideoCompressorUI(root)
    root.mainloop()

import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
from src.compressor import compress_video
from src.utils import check_ffmpeg, get_file_size
import os

class VideoCompressorUI:
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap("assets/logo.ico")
        self.root.title("Ultimate Video Compressor")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.input_path = ""
        self.output_path = ""
        self.crf_value = ctk.IntVar(value=28)

        self.setup_ui()

    def setup_ui(self):
        self.logo = ctk.CTkImage(light_image=Image.open("assets/logo.png"), size=(50, 50))
        ctk.CTkLabel(self.root, text=" Ultimate Video Compressor", image=self.logo, compound="left", font=("Helvetica", 20)).pack(pady=15)

        self.input_btn = ctk.CTkButton(self.root, text="Выбрать исходный файл", command=self.select_input)
        self.input_btn.pack(pady=10)

        self.input_label = ctk.CTkLabel(self.root, text="Исходный файл: не выбран")
        self.input_label.pack()

        self.output_btn = ctk.CTkButton(self.root, text="Выбрать выходной файл", command=self.select_output)
        self.output_btn.pack(pady=10)

        self.output_label = ctk.CTkLabel(self.root, text="Выходной файл: не выбран")
        self.output_label.pack()

        ctk.CTkLabel(self.root, text="Качество (CRF 0–51):").pack(pady=5)
        self.slider = ctk.CTkSlider(self.root, from_=0, to=51, number_of_steps=51, variable=self.crf_value)
        self.slider.pack(pady=5)

        self.compress_btn = ctk.CTkButton(self.root, text="СЖАТЬ ВИДЕО", command=self.start_compression)
        self.compress_btn.pack(pady=20)

        self.status = ctk.CTkLabel(self.root, text="Статус: ожидание")
        self.status.pack()

    def select_input(self):
        file = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mkv *.mov")])
        if file:
            self.input_path = file
            self.input_label.configure(text=f"Исходный: {os.path.basename(file)} ({get_file_size(file)})")

    def select_output(self):
        if not self.input_path:
            messagebox.showwarning("Нет исходного файла", "Пожалуйста, выберите исходный файл сначала.")
            return
        filename = f"compressed_{os.path.basename(self.input_path)}"
        file = filedialog.asksaveasfilename(defaultextension=".mp4", initialfile=filename)
        if file:
            self.output_path = file
            self.output_label.configure(text=f"Выходной: {os.path.basename(file)}")

    def start_compression(self):
        if not self.input_path or not self.output_path:
            messagebox.showerror("Ошибка", "Выберите входной и выходной файл.")
            return
        try:
            self.status.configure(text="Сжимаем...")
            compress_video(self.input_path, self.output_path, crf=self.crf_value.get())
            self.status.configure(text=f"Успешно! Размер: {get_file_size(self.output_path)}")
            messagebox.showinfo("Готово", f"Видео успешно сжато!\n\n{self.output_path}")
        except Exception as e:
            self.status.configure(text="Ошибка")
            messagebox.showerror("Ошибка", str(e))

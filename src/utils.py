import os
import subprocess


def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def get_file_size(path):
    try:
        size = os.path.getsize(path)
        return f"{size / (1024 * 1024):.2f} MB"
    except Exception:
        return "--"

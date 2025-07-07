import os
import subprocess
import sys

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return "ffmpeg"
    except (subprocess.CalledProcessError, FileNotFoundError):
        exe_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(sys.argv[0])))
        local_ffmpeg = os.path.join(exe_dir, "ffmpeg", "ffmpeg.exe")
        if os.path.isfile(local_ffmpeg):
            return local_ffmpeg
        else:
            raise FileNotFoundError("ffmpeg не найден. Убедитесь, что ffmpeg.exe лежит в папке 'ffmpeg' рядом с exe.")

# VideoSqueezeApp
Приложение для сжатия видео файлов

# 🔧 Структура проекта
```
video_compressor/
│
├── video_compressor/
│   ├── __init__.py
│   ├── app.py            # Главная логика приложения
│   ├── compressor.py     # Сжатие видео через FFmpeg
│   ├── ui.py             # Интерфейс на CustomTkinter
│   ├── utils.py          # Утилиты: размер файла, проверка FFmpeg и пр.
│
├── assets/
│   └── logo.png
│
├── requirements.txt      # Зависимости
├── Dockerfile            # Докер-сборка с ffmpeg внутри
└── main.py               # Точка входа
```

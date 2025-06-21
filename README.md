# 🎬 VideoSqueezeApp

Простое и удобное приложение на Python для **сжатия видеофайлов** с помощью FFmpeg.
Основано на **CustomTkinter** — современном GUI-интерфейсе с темной темой.
Поддерживает автоматическое определение битрейта, выбор пресетов и настройку качества вывода.

---

## 🚀 Возможности

* 📉 Сжатие видео без потери качества
* 🧠 Автоматический расчет целевого размера
* ⚙️ Настройка параметров сжатия (битрейт, CRF, пресеты)
* 🎛️ Графический интерфейс на CustomTkinter
* 📦 Экспорт в `.exe` с встроенным FFmpeg (Windows)
* 🐳 Поддержка Docker-сборки с FFmpeg

---

## 📁 Структура проекта

```bash
video_compressor/
│
├── video_compressor/
│   ├── __init__.py
│   ├── app.py            # Главная логика приложения
│   ├── compressor.py     # Работа с FFmpeg
│   ├── ui.py             # GUI на CustomTkinter
│   └── utils.py          # Вспомогательные функции
│
├── assets/
│   ├── logo.ico
│   └── logo.png
│
├── requirements.txt      # Зависимости проекта
├── Dockerfile            # Сборка в контейнере с ffmpeg
└── main.py               # Точка входа
```

---

## 🖥️ Установка и запуск

### 🔧 Установка зависимостей

```bash
pip install -r requirements.txt
```

> ⚠️ Убедитесь, что у вас установлен FFmpeg и доступен в `PATH`.

### ▶️ Запуск

```bash
python main.py
```

---

## 📦 Сборка EXE-файла (Windows)

### С PyInstaller:

```bash
pyinstaller --noconfirm --onefile --icon=assets/logo.ico main.py
```

> Чтобы FFmpeg работал в `.exe`, убедитесь, что `ffmpeg.exe` находится рядом с исполняемым файлом или встроен.

---

## 🐳 Docker

Соберите образ с уже установленным FFmpeg:

```bash
docker build -t video-compressor .
```

---

## 📤 GitHub Actions

Проект поддерживает автоматическую сборку `.exe` и загрузку в GitHub Releases.

> Не забудьте включить **Write permissions** в GitHub Actions и задать секрет `GH_TOKEN`, если используете `softprops/action-gh-release`.

---

## 📷 Скриншоты
![image](https://github.com/user-attachments/assets/170b175d-992d-48c0-b9e0-a1982fb20049)
![image](https://github.com/user-attachments/assets/7763aead-423e-43e4-b3d1-fa0dd50d03a0)


---

## 🛠️ Технологии

* Python 3.10+
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* FFmpeg
* PyInstaller (для сборки `.exe`)
* GitHub Actions

---

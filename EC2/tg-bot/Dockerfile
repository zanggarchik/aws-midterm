# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Устанавливаем переменные окружения (например, для токена бота)
#ENV TELEGRAM_BOT_TOKEN="your-telegram-bot-token"

# Запускаем бота
CMD ["python", "app.py"]

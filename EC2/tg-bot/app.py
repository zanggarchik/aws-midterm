from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

# Токен вашего Telegram бота
TOKEN = "<YOUR TG BOT TOKEN>"

# Функция для начала работы с процессом
def start_pipeline(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    update.message.reply_text("Запуск процесса анализа...")

    # Вызов Lambda или Step Function API (например)
    response = requests.post("<Lambda url>", json={})

    if response.status_code == 200:
        update.message.reply_text("Процесс анализа начался успешно!")
    else:
        update.message.reply_text("Не удалось запустить процесс анализа.")

# Обработчик команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я готов запускать процессы. Используйте команду /start_pipeline для начала.")

def main():
    # Создаем объект Updater и передаем ему ваш токен
    updater = Updater(TOKEN, use_context=True)

    # Получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем команду /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Регистрируем команду /start_pipeline для запуска процесса
    dispatcher.add_handler(CommandHandler("start_pipeline", start_pipeline))

    # Запускаем бота
    updater.start_polling()

    # Ожидаем остановки работы
    updater.idle()

if __name__ == '__main__':
    main()

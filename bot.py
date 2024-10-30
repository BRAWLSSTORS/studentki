import os
import subprocess
import sys

# Функция для установки пакета
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Устанавливаем telebot, если он не установлен
try:
    import telebot
except ImportError:
    print("Устанавливаю pyTelegramBotAPI...")
    install_package('pyTelegramBotAPI')
    import telebot
    print("pyTelegramBotAPI успешно установлен!")

# Получаем токен из переменных окружения
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    raise ValueError("Токен Telegram бота не найден! Убедитесь, что переменная окружения TELEGRAM_BOT_TOKEN установлена.")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой новый телеграм бот. Рад тебя видеть! 👋")

if __name__ == '__main__':
    print("Бот запущен!")
    bot.infinity_polling()

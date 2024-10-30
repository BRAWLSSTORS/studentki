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

# Прямой ввод токена
TOKEN = '7368730334:AAHrLFjgLQP_PBYRdYkDW5H7QoiZHbBzoUc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой новый телеграм бот. Рад тебя видеть! 👋")

if __name__ == '__main__':
    print("Бот запущен!")
    bot.infinity_polling()

import random
from telegram.ext import Updater, CommandHandler

films = [
    "Гарри Поттер",
    "Слуга народа",
    "Бумер",
    "Один дома",
    "Жмурки",
    "Бригада",
    "Анжела Перл – расклад на год 💅",
    "Данила Поперечный: АГЕНТ 813"
]

def start(update, context):
    update.message.reply_text(
        "Привет! Напиши /film, чтобы я выбрал фильм на сегодня 🎬"
    )

def film(update, context):
    movie = random.choice(films)
    update.message.reply_text(f"Сегодня ты смотришь: 🎥 {movie}")

def main():
    token = "8476573533:AAHr9iIMr1jw-wwJ9YOx3DfRL3tc1iNwGLQ"   # ← ВСТАВИЛ ТВОЙ ТОКЕН

    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("film", film))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

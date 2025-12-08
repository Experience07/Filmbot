import random
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Напиши /film чтобы я выбрал фильм на сегодня 🎬"
    )

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE):
    movie = random.choice(films)
    await update.message.reply_text(f"Сегодня ты смотришь: 🎥 {movie}")

def main():
    # Получаем токен из переменной окружения на Render
    TOKEN = os.getenv("BOT_TOKEN")

    if TOKEN is None:
        raise ValueError("❌ Ошибка: переменная окружения BOT_TOKEN не установлена!")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("film", film))

    app.run_polling()

if __name__ == "__main__":
    main()

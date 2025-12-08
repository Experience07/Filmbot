import random
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
    await update.message.reply_text("Привет! Напиши /film, чтобы я выбрал фильм на сегодня 🎬")

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE):
    movie = random.choice(films)
    await update.message.reply_text(f"Сегодня ты смотришь: 🎥 {movie}")

def main():
    token = "8476573533:AAEwO2smXP77_v7PzptHSWC90rzgRvH-cgI"

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("film", film))

    app.run_polling()

if __name__ == "__main__":
    main()

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 مرحباً بك في Maroc Education Bot\n\n"
        "📢 هذا البوت سيرسل آخر الأخبار الرسمية:\n"
        "• مذكرات وزارة التربية الوطنية\n"
        "• إعلانات الدكتوراه\n"
        "• مباريات التعليم\n"
        "• البلاغات الرسمية"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

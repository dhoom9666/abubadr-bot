from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os
TOKEN = os.getenv("TOKEN")  # نجيب التوكن من Environment Variables

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً! أنا شغال 24/7 🔥")

# الردود على أي رسالة
async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "سلام" in text:
        await update.message.reply_text("وعليكم السلام 🌸")
    else:
        await update.message.reply_text(f"قلت: {text}")

# إنشاء البوت
app = ApplicationBuilder().token(TOKEN).build()

# إضافة الأوامر والردود
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))

# هذا السطر المهم: يشغل Polling
app.run_polling()

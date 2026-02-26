import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
import os

# التوكن من Secrets في Replit
TOKEN = os.getenv("TOKEN")

# --- أوامر ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("نكتة", callback_data='joke')],
        [InlineKeyboardButton("اقتباس", callback_data='quote')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "أهلاً يا أبو بدر! 🤖🔥\nاختر زر أو اكتب رسالة للتفاعل معي",
        reply_markup=reply_markup
    )

# --- الردود على الرسائل ---
async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.is_bot:
        return

    text = update.message.text.lower()

    if "سلام" in text:
        await update.message.reply_text("وعليكم السلام 🌸")
    elif "كيفك" in text:
        await update.message.reply_text("تمام الحمدلله 😎")
    elif "نكتة" in text:
        await send_joke(update)
    elif "اقتباس" in text:
        await send_quote(update)
    else:
        await update.message.reply_text(f"قلت: {update.message.text}")

# --- إرسال نكتة ---
async def send_joke(update):
    jokes = [
        "😂 ليش الكمبيوتر ما يلعب كرة؟ لأنه يخاف من الفيروسات!",
        "😅 مرة واحد برمج… طلع له Error!",
        "🤣 المعلم قال للتلميذ: صح ولا غلط؟ قال التلميذ: Ctrl+Z!"
    ]
    await update.message.reply_text(random.choice(jokes))

# --- إرسال اقتباس ---
async def send_quote(update):
    quotes = [
        "💪 الثقة بالنفس سر النجاح",
        "🌱 من جد وجد ومن زرع حصد",
        "✨ لا تتوقف عن المحاولة أبداً"
    ]
    await update.message.reply_text(random.choice(quotes))

# --- الرد على الأزرار ---
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "joke":
        await send_joke(query)
    elif query.data == "quote":
        await send_quote(query)

# --- تشغيل البوت ---
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))
app.add_handler(CallbackQueryHandler(button))

print("Bot is running 24/7 on Replit...")
app.run_polling()

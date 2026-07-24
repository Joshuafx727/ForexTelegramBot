from analysis import analyze_pair
from telegram.ext import Application, CommandHandler, ContextTypes
from config import TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to Coach Josh AI Forex Bot!\n\n"
        "Commands:\n"
        "/start - Start the bot\n"
        "/help - Help\n"
        "/analyze EURUSD - Analyze a pair"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Example:\n"
        "/analyze EURUSD\n"
        "/analyze GBPUSD\n"
        "/analyze XAUUSD"
    )

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text(
            "Usage:\n/analyze EURUSD"
        )
        return

    pair = context.args[0].upper()

    result = analyze_pair(pair)

    message = f"""
📊 {pair} Analysis

Trend: {result['trend']}

Entry: {result['entry']}
Stop Loss: {result['stop_loss']}

Take Profit: {result['take_profit']}
"""
    await update.message.reply_text(message)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("analyze", analyze))

    print("Bot Started Successfully...")

    app.run_polling()

if __name__ == "__main__":
    main()
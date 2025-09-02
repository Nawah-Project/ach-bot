from telegram import Update ,InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters,InlineQueryHandler
from data_manager import Data_Manager as DB , Bot_Setting as BS
import os
from commands.set_group import set_group
from commands.set_monitoring_topic import set_monitoring_topic
from commands.set_notification_topic import set_notification_topic
from commands.set_rules_topic import set_rules_topic
from commands.massage_handler import monitoring_topic , new_user
from commands.state import state
from commands.set_timer import set_timer
from commands.restart_missed import restart_missed
BOT_TOKEN = os.getenv("BOT_TOKEN")
import logging

# تعطيل اللوجات من مكتبة httpx
logging.getLogger("httpx").setLevel(logging.WARNING)
    
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("set_group", set_group))
app.add_handler(CommandHandler("set_monitoring_topic", set_monitoring_topic))
app.add_handler(CommandHandler("set_notification_topic", set_notification_topic))
app.add_handler(CommandHandler('set_rules_topic', set_rules_topic))
app.add_handler(CommandHandler('restart_missed', restart_missed))
app.add_handler(CommandHandler('state', state))
app.add_handler(MessageHandler(filters.ChatType.GROUPS & filters.StatusUpdate.NEW_CHAT_MEMBERS, new_user))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitoring_topic))
app.add_handler(CommandHandler('set_timer', set_timer))


app.run_polling()
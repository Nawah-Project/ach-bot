from telegram import Update
from telegram.ext import ContextTypes
from data_manager import Data_Manager as DM
from utils import is_admin



async def restart_missed(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    if await is_admin(update, context, user_id) :
        DM().weekly_missed_update(chat_id)
        await context.bot.send_message(chat_id, text="تم عمل التشيك الأسبوعي ✅")
    else:
        await update.message.reply_text("ليس لديك صلاحية")
    
    
from telegram import Update
from telegram.ext import ContextTypes
from data_manager import Data_Manager as DM
from utils import is_admin
import  datetime
from zoneinfo import ZoneInfo

async def weekly_check(context : ContextTypes.DEFAULT_TYPE):
    job = context.job
    chat_id = job.chat_id
    DM().weekly_missed_update(chat_id)
    await context.bot.send_message(chat_id, text="تم عمل التشيك الأسبوعي ✅")
    
async def set_timer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    if await is_admin(update, context, user_id):                       
        context.job_queue.run_daily(                        
            weekly_check,            
            time=datetime.time(tzinfo=ZoneInfo("Africa/Cairo")),  
            days=(6,),  
            name=str(chat_id),                   
            chat_id=chat_id,
            
        )
        await update.message.reply_text("تم تفعيل التشيك الأسبوعي ✅")
    else:
        await update.message.reply_text("❌ ليس لديك صلاحية")

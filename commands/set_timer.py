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
    app_info = await context.bot.get_me()
    bot_link = f"https://t.me/{app_info.username}?start=weekly_sub"
    msgg = "مرحبًا يا أبطال! حبيت أفكركم إن أسبوع جديد بدء و الوقت حان عشان تشاركوا إنجازاتكم الأسبوعية 📝\n"
    msg = await context.bot.send_message(
    chat_id,
    text=msgg + f'👋 وعشان توصلك التنبيهات في الخاص اضغط <a href="{bot_link}">اشتراك</a>',
    parse_mode="HTML")
    await context.bot.pin_chat_message(chat_id,msg.id)

    
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
        await update.message.reply_text("تم تفعيل التذكير الأسبوعي ✅")
    else:
        await update.message.reply_text("❌ ليس لديك صلاحية")

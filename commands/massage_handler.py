from telegram import Update
from telegram.ext import ContextTypes
from data_manager import Data_Manager as DB , Bot_Setting as BS
from achievement import Achievement



async def monitoring_topic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    chat_id = update.effective_chat.id    
    monitoring_topic_id = BS().get_monitoring_topic_id(chat_id)
    if update.message.message_thread_id is monitoring_topic_id:
        await submit_achievement(update, context)
    

async def new_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    DB().check_user_id(user_id, chat_id)
    
async def submit_achievement(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    points  = 7
    if Achievement().check_achievement(update.message.text):
        if DB().get_missed(user_id, chat_id) > 0:
            DB().update_user_count(user_id, chat_id, points)
            DB().update_user_missed(user_id, chat_id)
           
            user_scor = DB().state_count(user_id, chat_id)
            message = f"🏆 تم تسجيل إنجازك بنجاح! 🎉\n\n✨ نقاطك الحالية: {user_scor} نقطة ✨"
            await update.message.reply_text(message)
        else:
            await update.message.reply_text(
                "⚠️ لقد سجّلت إنجازك هذا الأسبوع بالفعل.\n"
                "⏳ لا يمكن تسجيل أكثر من مرة في نفس الأسبوع."
            )
    else:
        await update.message.reply_text(
            "📝 تذكير مهم:\n\n"
            "المكان ده مخصص فقط لتسجيل **الإنجازات الأسبوعية** ✅\n"
            "عند إرسال الإنجاز لازم تحتوي الرسالة على:\n"
            "🔹 كلمة *الإنجاز الأسبوعي* أو\n"
            "🔹 كلمة *الإنجاز* لوحدها."
        )

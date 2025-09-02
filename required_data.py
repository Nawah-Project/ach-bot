from telegram import Update

class Required_data :
    def __init__(self, update: Update) :
        self.user_id     = update.effective_user.id
        self.username = update.effective_user.username or update.effective_user.first_name
        self.chat_id = update.effective_chat.id
        self.current_thread_id = update.message.message_thread_id
        self.text = update.message.text #the acheivement massage
            

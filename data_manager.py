import sqlite3
import os
from dotenv import load_dotenv
import logging

load_dotenv()  # يقرأ .env
DB = os.getenv("DB")
class Data_Manager:

    """
    This class is used to manage the data in the database.
    """
    def __init__(self,):
      
        self.con = sqlite3.connect(DB)
        self.cur = self.con.cursor()

    def state_count(self,user_id,chat_id):
        """To get the user achievement score"""
        logging.info(f"xuser_id={user_id}, xchat_id={chat_id}")
        count = self.cur.execute("SELECT score FROM user_state WHERE user_id = ? AND chat_id = ?", (user_id,chat_id))       
        scorex = count.fetchone()
        logging.info(f"scorex={scorex}")
        score = scorex[0]
        logging.info(f"score={score},")
        return score
    

        
    def add_new_user(self,user_id,chat_id):
        """To add a new user to the database"""
        score = 0
        missed = 1
        is_subscribed = False

        data = [
        (chat_id, user_id, score, missed, is_subscribed)]
        self.cur.executemany("INSERT INTO user_state VALUES(?, ?, ?, ? ,?)", data)

        self.con.commit()  # Remember to commit the transaction after executing INSERT.

    def update_user_count(self,user_id, chat_id,points):
        """To add a new user to the database"""
        count = self.cur.execute("SELECT score FROM user_state WHERE user_id = ? AND chat_id = ?", (user_id,chat_id))
        self.con.commit()
        score = count.fetchone()[0]
        new_score = score + points 
        self.cur.execute("""
        UPDATE user_state
        SET score = ?
        WHERE user_id = ? AND chat_id = ?
        """, (new_score, user_id, chat_id))
        self.con.commit()
    
    def update_user_missed(self,user_id,chat_id,):
        """To update the user missed score"""
      
        self.cur.execute("""
        UPDATE user_state
        SET missed = ? 
        WHERE 
        user_id = ? AND chat_id = ?
        """, (0, user_id, chat_id))
        self.con.commit()
    def weekly_missed_update(self,chat_id,):
        """To beggin a new week"""
        res = self.cur.execute("SELECT missed, user_id FROM user_state WHERE chat_id = ?", (chat_id,))
        r = res.fetchall()
        for user in range(len(r)):
            new_missed = r[user][0] + 1
            user_id = r[user][1]
            self.cur.execute("""
            UPDATE user_state
            SET missed = ? 
            WHERE 
            user_id = ?
            """, (new_missed,user_id))
            self.con.commit()
    def get_missed(self,user_id, chat_id):
        """To get the user missed score"""
        missed = self.cur.execute("SELECT missed FROM user_state WHERE user_id = ? AND chat_id = ?", (user_id, chat_id,))
        user_missed = missed.fetchone()[0]
        return user_missed
    def check_user_id(self,user_id, chat_id):
        """To check if the user is in the database"""
        res = self.cur.execute("SELECT user_id FROM user_state WHERE chat_id = ?", (chat_id,))
        self.con.commit()
        user_ids = []
        for id in res.fetchall():
            id[0]    
            user_ids.append(id[0])            
        if user_id not in set(user_ids) or user_ids == []:   
            self.add_new_user(user_id, chat_id)
        

class Bot_Setting(Data_Manager):
    """to set the bot setting in a specific group"""

    def __init__(self,):
        super().__init__()
        
    

    def add_new_group(self,chat_id):
        """To add a new group to the database"""
        monitoring_topic = 1
        notification_topic = 0
        rules_topic = 0

        data = [
        (chat_id, monitoring_topic, notification_topic, rules_topic)]
        self.cur.executemany("INSERT INTO bot_setting VALUES(?, ?, ?, ?)", data)

        self.con.commit()  # Remember to commit the transaction aft
    def check_group_id(self, chat_id):
        """To check if the user is in the database"""
        res = self.cur.execute("SELECT chat_id FROM bot_setting")
        groups_ids = []
        for id in res.fetchall():
            id[0]    
            groups_ids.append(id[0])   
               
        if chat_id not in set(groups_ids) or groups_ids == []:   
            self.add_new_group(chat_id)

    def add_monitoring_topic_id(self,monitoring_topic_id, chat_id,):
        """To add a new user to the database"""  
        self.cur.execute("""
        UPDATE bot_setting
        SET monitoring_topic = ?
        WHERE chat_id = ?
        """, (monitoring_topic_id, chat_id))
        self.con.commit()

    def add_notification_topic_id(self,notification_topic_id, chat_id,):
        """To add a new user to the database"""  
        self.cur.execute("""
        UPDATE bot_setting
        SET notification_topic = ?
        WHERE chat_id = ?
        """, (notification_topic_id, chat_id))
        self.con.commit()        
        

    def add_rules_topic_id(self,rules_topic_id, chat_id,):
        """To add a new user to the database"""  
        self.cur.execute("""
        UPDATE bot_setting
        SET rules_topic = ?
        WHERE chat_id = ?
        """, (rules_topic_id, chat_id))
        self.con.commit()

    def get_monitoring_topic_id(self, chat_id):
        """To get the monitoring topic id"""
        return self.cur.execute("SELECT monitoring_topic FROM bot_setting WHERE chat_id = ?", (chat_id,)).fetchone()[0]

    def get_notification_topic_id(self, chat_id):
        """To get the notification topic id"""
        return self.cur.execute("SELECT notification_topic FROM bot_setting WHERE chat_id = ?", (chat_id,)).fetchone()[0]

    def get_rules_topic_id(self, chat_id):
        """To get the rules topic id"""
        return self.cur.execute("SELECT rules_topic FROM bot_setting WHERE chat_id = ?", (chat_id,)).fetchone()[0]
import datetime , time 
from data_manager import Data_Manager
DM = Data_Manager()
class Achievement:
    def __init__(self,):
        
        achievement_keywords = ["الإنجاز", "الأنجاز", "الانجاز", "أنجاز", "إنجاز", "انجاز", "إنجازي", "انجازي", "أنجازي", "الإنجازي"]
        week_keywords = ["الأسبوع", "الاسبوع", "أسبوع", "اسبوع", "الأسبوعي", "الاسبوعي", "أسبوعي", "اسبوعي"]
        self.requirded_keywords = achievement_keywords + week_keywords
    def check_achievement(self,massage):
        keywords = self.requirded_keywords
        state = False
        for keyword in keywords :
            if keyword in massage :
                state = True
                break
        return state
    


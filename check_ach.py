import datetime , time 
from data_manager import Data_Manager
DM = Data_Manager()
class CheckAchievement:
    def __init__(self,):
        
        self.study_keywords = ["دراسي", "دراسية", "الدراسي", "الدراسية","الدراسة", "دراسة", "للدراسة", "دراستي", "دراسيةً","مذاكرة", "مذاكرتي", "للمذاكرة"]
        self.week_keywords = ["الأسبوع", "الاسبوع", "أسبوع", "اسبوع", "الأسبوعي", "الاسبوعي", "أسبوعي", "اسبوعي"]
        
    def check_achievement(self,massage,points):
        if points == 70:
            keywords = self.week_keywords
        else:
            keywords = self.study_keywords
        state = False
        for keyword in keywords :
            if keyword in massage :
                state = True
                break
        return state
    


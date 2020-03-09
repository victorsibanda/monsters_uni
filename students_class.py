from monsters_class import *

class Students(Monsters):


    def __init__(self,f_name,l_name,skills,__student_id):
        super().__init__(f_name,l_name,skills)
        self.__student_id = __student_id




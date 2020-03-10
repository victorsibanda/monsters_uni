from monsters_class import *


class Students(Monsters):

    def __init__(self, f_name, l_name, student_id ):
        super().__init__(f_name, l_name)
        self.student_id = student_id


    def add_skill(self,skills):
        self.skills.append(skills)

def add_skill(student,skill_list):
    for i in skill_list :
        student.add_skills(i)



# student1 = Students('John','Fisher',1)
#
# student1.skills.append('Run')
#
# print(student1.skills)
#
# add_skill(student1,'Jog')
# print(student1.skills)


from monsters_class import *


class Students(Monsters):

    def __init__(self, f_name, l_name, student_id):
        super().__init__(f_name, l_name)
        self.student_id = student_id




def add_skill(student,skill_list):
    for i in skill_list :
        student.add_skills(i)


# f_name = input('Fname')
# l_name = input('Lname')
#
# student2 = Students(f_name,l_name,1)
#
# print

# student1 = Students('John','Fisher',1)
#
# student1.skills.append('Run')
#
# print(student1.skills)
#
# add_skill(student1,'Jog')
# print(student1.skills)


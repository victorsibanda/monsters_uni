from monsters_class import *


class Students(Monsters):

    def __init__(self, f_name, l_name, __student_id):
        super().__init__(f_name, l_name)
        self.__student_id = __student_id

    def get_student_id(self):
        __student_id = 1
        __student_id += 1
        return





from monsters_class import *


class Teachers(Monsters):

    def __init__(self, f_name, l_name, skills, __staff_id):
        super().__init__(f_name, l_name, skills)
        self.__staff_id = __staff_id

    def get_staff_id(self):
        __staff_id = 1
        __staff_id += 1
        return



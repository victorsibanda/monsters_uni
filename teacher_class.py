from monsters_class import *


class Teachers(Monsters):

    def __init__(self, f_name, l_name, skills, __staff_id):
        super().__init__(f_name, l_name, skills)
        self.__staff_id = __staff_id
class Monsters():

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.skills = []

    def add_skill(self,skills):
        self.skills.append(skills)
        return "New skill:" + skills

    # def invisibility(self):
    #     return
    #
    # def loud_roar(self):
    #     return
    #
    # def sneak(self):
    #     return



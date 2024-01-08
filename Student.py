class Student:

    def __init__(self,name,major,gpa,is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

class Question:

    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer


class Chef:

    def make_chicken(self):
        print("The chef makes a chiken")

    def make_soup(self):
        print("The chef makes a soup")

    def make_special(self):
        print("The chef makes a fish")

class SuperChef(Chef):

    def make_rice(self):
        print("The chef makes a rice")

    def make_special(self):
        print("The chef makes a wakame")
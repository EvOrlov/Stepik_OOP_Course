class Person:
    gend = {'male':'Гражданин','female':'Гражданка'}
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        self.gender = gender
        if self.gender not in Person.gend.keys():
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = 'male'

    def __str__(self):
        return f"{Person.gend[self.gender]} {self.surname} {self.name}"
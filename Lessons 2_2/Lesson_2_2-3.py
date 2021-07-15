class SoccerPlayer:
    def __init__(self, name, surname, goals = 0, assists = 0):
        self.name = name
        self.surname = surname
        self. goals = goals
        self.assists = assists

    def score(self, new_goals = 1, ):
        self.goals += new_goals

    def make_assist(self, new_assist = 1, ):
        self.assists += new_assist

    def statistics(self):
        print(f"{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}")
class Zebra:
    def __init__(self):
        self.color = "Полоска белая"
    def which_stripe(self):
        print(self.color)
        if self.color == "Полоска белая": self.color = "Полоска черная"
        else: self.color = "Полоска белая"

class CheckPassword:
    path_to_txt = "pass.txt"

    def __init__(self, password):
        self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.not_in_pass_list(value):
            self.__password = value
            print(self.__password)
        else:
            raise ValueError("Небезопасный пароль")

    @staticmethod
    def not_in_pass_list(value):
        with open(CheckPassword.path_to_txt, 'r') as file:
            passlist = map(str.strip, file.readlines())
        if value in passlist:
            return False
        else:
            return True

s = CheckPassword("1wrghh4th")
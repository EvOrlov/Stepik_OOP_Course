class UserMail:
    def __init__(self, login, mail):
        self.login = login
        self.__email = mail

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if isinstance(new_email, str) and new_email.count("@") == 1 and "." in new_email[new_email.find("@"):]:
            self.__email = new_email
        else:
            print("Ошибочная почта")

    email = property(fget=get_email, fset=set_email)

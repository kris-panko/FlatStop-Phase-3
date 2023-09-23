class Shopper:
    def __init__(self, user_name, age):
        self.user_name = user_name
        self.age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if isinstance(age, int) and age > 12:
            self._age = age
        else:
            print("Sorry, age needs to be a valid number and greater than 12")
    @property
    def user_name(self):
        return self._user_name
    @user_name.setter
    def user_name(self, user_name):
        if isinstance(user_name, str) and len(user_name) > 3:
            self._user_name = user_name
        else:
            print("Please try entering username again: Must be a string and greater than 3 characters long")
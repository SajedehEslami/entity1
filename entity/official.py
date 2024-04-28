from entity.employee import Employee

list_username = []


# Inheritance
class Official(Employee):
    def __init__(self, name, family, national_code, user_name, password):
        super().__init__(name, family, national_code)
        self.user_name = user_name
        self.password = password

    # Encapsulation
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        if user_name not in list_username:
            list_username.append(user_name)
            self._user_name = user_name
        else:
            raise ValueError("Exist!!!")

from entity.official import Official



# Inheritance
class Mailroom(Official):
    def __init__(self, name, family, national_code, user_name, password, access_level):
        super().__init__(name, family, national_code, user_name, password)
        self.access_level = access_level

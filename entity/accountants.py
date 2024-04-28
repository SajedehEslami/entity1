from entity.financial import Financial



# Inheritance
class Accountants(Financial):
    def __init__(self, name, family, national_code, validity,access_level):
        super().__init__(name, family, national_code,validity)
        self.access_level = access_level



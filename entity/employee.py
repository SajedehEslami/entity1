import re

list_national_code = []


# Abstraction
class Employee:

    def __init__(self, name, family, national_code):
        self.name = name
        self.family = family
        self.national_code = national_code

    # Encapsulation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if re.match("^[A-Za-z]+$", name):
            self._name = name
        else:
            raise ValueError("Error!!!")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        if re.match("^[A-Za-z]+$", family):
            self._family = family
        else:
            raise ValueError("Error!!!")

    @property
    def national_code(self):
        return self._national_code

    @national_code.setter
    def national_code(self, national_code):
        if re.match("\\d{3}-\\d{2}-\\d{4}", national_code) and (national_code not in list_national_code):
            list_national_code.append(national_code)
            self._national_code = national_code

        else:
            raise ValueError("Error!!!")

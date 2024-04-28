from entity.employee import Employee
import re


# Inheritance
class Financial(Employee):
    def __init__(self, name, family, national_code, validity):
        super().__init__(name, family, national_code)
        self.validity = validity

    # Encapsulation
    @property
    def validity(self):
        return self._validity

    @validity.setter
    def validity(self, validity):
        if re.match("^\\d+$", validity):
            self._validity = validity
        else:
            raise ValueError("Error!!!")

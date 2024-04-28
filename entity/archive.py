from entity.official import Official
import re


# Inheritance
class Archive(Official):
    def __init__(self, name, family, national_code, user_name, password, floor):
        super().__init__(name, family, national_code, user_name, password)
        self.floor = floor

    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, floor):
        if re.match("^\\d+$", floor):
            self._floor = floor
        else:
            raise ValueError("Error!!")

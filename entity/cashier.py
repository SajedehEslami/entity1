from entity.financial import Financial
import re


# Inheritance
class Cashier(Financial):
    def __init__(self, name, family, national_code, validity, fund_number):
        super().__init__(name, family, national_code, validity)
        self.fund_number = fund_number

    # Encapsulation
    @property
    def fund_number(self):
        return self._fund_number

    @fund_number.setter
    def fund_number(self, fund_number):
        if re.match("^\\d+$", fund_number):
            self._fund_number = fund_number
        else:
            raise ValueError("Error!!! ")

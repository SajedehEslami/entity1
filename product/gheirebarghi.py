from product import Kala

class NoElectrical(Kala):

    def __init__(self,vazn,gheimat,shomareserial,mahalemasraf):
        super().__init__(vazn,gheimat,shomareserial)
        self.mahalemasraf =mahalemasraf


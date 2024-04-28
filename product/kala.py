
class Kala:
    def __init__(self,vazn,gheimat,shomareserial):
        self.vazn=vazn
        self.gheimat=gheimat
        self.shomareserial=shomareserial
    #def set_vazn(self,vazn):
        #if vazn>0:
            #self._vazn=vazn
        #else:
            #raise ValueError("moteasfam")
    #def get_vazn(self):
        #return self._vazn


    #vazn=property(get_vazn,set_vazn)
    @property
    def vazn(self):
        return self._vazn

    @vazn.setter
    def vazn(self, vazn):
        if vazn > 0:
            self._vazn=vazn
        else:
            raise ValueError("moteasfam")

import re

class Person:
    def __init__(self,name,family,id):
        self.name = name
        self.family =family
        self.id = id

    def getName(self):
        return self._name

    def setName(self,name):
        if re.match("^[A-Za-z]+$",name):
            self._name= name
        else:
            raise ValueErroral("Invalid")

    def to_tuple(self):
        return(self.name,self.family,self.id)
    name = property(fget=getName,fset=setName)
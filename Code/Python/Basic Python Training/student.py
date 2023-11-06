#OOPS

class Student:

    number_of_Students = 0

  
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    def getage(self):
        return self.__age

    def getname(self):
        return self.__name

    def incrementAge(self,n):
        self.__age = self.__age + n
    
    def increment_total_object():
        number_of_Students  = number_of_Students + 1




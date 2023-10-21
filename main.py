###class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.hapiness = 100
#        self.age = age
#        self.money = 1000
#class Student(Person):
 #   def __init__(self):
 #       def __init__(self):
##            super().__init__()
 #   def rest(self):
#        self.hapiness += 10
#student = Student('Bob')
#student1 = Student('Jack')
#student.rest()
#student1.rest()
##print(student.name, student.hapiness)
###










class Square:
    def __init__(self, side):
        self.side = side

    def s(self):
        return self.side ** 2


class Priamo(Square):
    def __init__(self, side, side1):
        super().__init__(side)
        self.side1 = side1
    def s(self):
        return self.side * self.side1




square = Square(10)
p = Priamo(10,20)
print(p.s())
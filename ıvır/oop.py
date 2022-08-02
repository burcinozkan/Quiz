# class Circle:
#     pi=3.14
#
#     def __init__(self, radius=1):
#         self.radius=radius
#
#     def perimeter(self):
#         return 2*self.pi*self.radius
#
#     def area(self):
#         return self.pi*(self.radius**2)
#
# c1=Circle()
# c2=Circle(2)
# print("c1's perimeter {} : area{}".format(c1.perimeter(),c1.area()))
# print("c2's perimeter {} : area {}".format(c2.perimeter(),c2.area()))
class Person():
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
        print("Person created")

class Student(Person):
    def __init__(self, fname, lname):

        super().__init__(fname, lname)
        print("student created")


s1=Student("ali", "yılmaz")
print("name: {}, surname: {}".format(s1.fname,s1.lname))
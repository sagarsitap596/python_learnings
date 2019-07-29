#
# Multiple constructors not allowed
#

from pprint import pprint
import datetime

class Student:

    phone=None
    dob=datetime.date.today()
    name=None
    totalMarks=None

    def __init__(self,name,totalMarks,phone,dob):
        self.totalMarks =totalMarks
        self.name=name
        self.phone=phone
        self.dob=dob

    def getMarks(self):
        return self.totalMarks;
    def getName(self):
        return self.name;
    def getPhone(self):
        return self.phone
    def getDOB(self):
        return self.dob


class SportStudent(Student):

    sportName=""
    def __init__(self,sportName,name,totalMarks,phone,dob):
        print("I am SportStudent")
        self.sportName=sportName
        self.totalMarks = totalMarks
        self.name = name
        self.phone = phone
        self.dob = dob


stud=Student("sagar",84.17,9029335578,datetime.datetime(1993,11,16,00,49,43))
pprint(vars(stud))
print(stud.getName())
print(stud.getMarks())
print(stud.getPhone())
print(stud.getDOB())
print("-"*50)

sportStudent=SportStudent("Cricket","sagar1",79.69,9967674699,datetime.datetime(1993,11,16,00,49,44))
print(sportStudent.sportName)
print(sportStudent.getName())
print(sportStudent.getMarks())
print(sportStudent.getPhone())
print(sportStudent.getDOB())




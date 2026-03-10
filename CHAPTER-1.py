'''
"Python Learning"
Learning: "BASIC-OOPS-concept-Class,Object,method,function"
DAY01-Task

'''
from datetime import datetime
class Student:
    def __init__(self, name,roll_no,dob,standard,total_marks,grade,gender):
        self.name=name
        self.roll_no=roll_no
        self.dob=dob
        self.standard=standard
        self.total_marks=total_marks
        self.grade=grade
        self.gender=gender
    def display(self):
        print("student name is:", self.name)
        print("student Roll.no is:", self.roll_no)
        print("student age is:",self.get_age())
        print("student- current standard is:",self.standard)
        print("student total marks(out of 500)is:",self.total_marks)
        print("student grade is :",self.grade)
        print("student gender is :",self.gender)
    def get_age(self):
        today = datetime.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age
print("CLASS_A_STUDENT_DETAILS:")
print()
student1_classA=Student("Abinaya","Roll.no: 1",datetime(2016, 3, 1),"5th standard",300,"C","Female")
student1_classA.display()
student2_classA=Student("Ashika","Roll.no: 2",datetime(2016, 1, 22),"5th standard",467,"B+","Female")
student2_classA.display()
student3_classA=Student("Bala","Roll.no: 3",datetime(2014, 1, 23),"5th standard",480,"A","Male")
student3_classA.display()
student4_classA=Student("Cindhya","Roll.no: 4",datetime(2015, 2, 15),"5th standard",415,"B","Female")
student4_classA.display()
student5_classA=Student("Deepan","Roll.no: 5",datetime(2015, 1, 15),"5th standard",498,"A+","Male")
student5_classA.display()
print()
print("CLASS_B_STUDENT_DETAILS:")
print()
student6_classB=Student("Gowtham","Roll.no: 6",datetime(2014, 11, 15),"5th standard",499,"A+","Male")
student6_classB.display()
student7_classB=Student("Harini","Roll.no: 7",datetime(2015, 10, 15),"5th standard",322,"C","Female")
student7_classB.display()
student8_classB=Student("Kishore","Roll.no: 8",datetime(2014, 5, 15),"5th standard",491,"A+","Male")
student8_classB.display()
student9_classB=Student("Maran","Roll.no: 9",datetime(2015, 9, 20),"5th standard",400,"B","Male")
student9_classB.display()
student10_classB=Student("Sayesha","Roll.no: 10",datetime(2016, 6, 17),"5th standard",460,"B+","Female")
student10_classB.display()
print()










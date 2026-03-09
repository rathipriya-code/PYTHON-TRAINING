'''
"Python Learning"
Learning: "BASIC-OOPS-concept-Class,Object,method,function"
DAY01-Task

'''
class Class_A:
    def __init__(self, name,roll_no,age,standard,total_marks,grade,gender):
        self.name=name
        self.roll_no=roll_no
        self.age=age
        self.standard=standard
        self.total_marks=total_marks
        self.grade=grade
        self.gender=gender
    def student_details(self):
        print("student name is:", self.name)
        print("student Roll.no is:", self.roll_no)
        print("student age is:",self.age)
        print("student- current standard is:",self.standard)
        print("student total marks(out of 500)is:",self.total_marks)
        print("student grade is :",self.grade)
        print("student gender is :",self.gender)
print("CLASS_A_STUDENT_DETAILS:")
print()
student1_classA=Class_A("Abinaya","Roll.no: 1",10,"5th standard",300,"C","Female")
student1_classA.student_details()
student2_classA=Class_A("Ashika","Roll.no: 2",11,"5th standard",467,"B+","Female")
student2_classA.student_details()
student3_classA=Class_A("Bala","Roll.no: 3",11,"5th standard",480,"A","Male")
student3_classA.student_details()
student4_classA=Class_A("Cindhya","Roll.no: 4",10,"5th standard",415,"B","Female")
student4_classA.student_details()
student5_classA=Class_A("Deepan","Roll.no: 5",11,"5th standard",498,"A+","Male")
student5_classA.student_details()
class Class_B:
    def __init__(self, name, roll_no, age, standard, total_marks, grade, gender):
        self.class_B=Class_A(name,roll_no, age, standard, total_marks, grade, gender)
    def student_details_classB(self):
        self.class_B.student_details()
print()
print("CLASS_B_STUDENT_DETAILS:")
print()
student1_classB=Class_B("Gowtham","Roll.no: 6",12,"5th standard",499,"A+","Male")
student1_classB.student_details_classB()
student2_classB=Class_B("Harini","Roll.no: 7",12,"5th standard",322,"C","Female")
student2_classB.student_details_classB()
student3_classB=Class_B("Kishore","Roll.no: 8",11,"5th standard",491,"A+","Male")
student3_classB.student_details_classB()
student4_classB=Class_B("Maran","Roll.no: 9",10,"5th standard",400,"B","Male")
student4_classB.student_details_classB()
student5_classB=Class_B("Sayesha","Roll.no: 10",12,"5th standard",460,"B+","Female")
student5_classB.student_details_classB()










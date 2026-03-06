class Class_A:
    def __init__(self, name,age,standard,total_marks,grade,gender):
        self.name=name
        self.age=age
        self.standard=standard
        self.total_marks=total_marks
        self.grade=grade
        self.gender=gender
    def student1_details(self):
        print("student1 name is:", self.name)
        print("student1 age is:",self.age)
        print("student1- current standard is:",self.standard)
        print("student1 total marks(out of 500)is:",self.total_marks)
        print("student1 grade is :",self.grade)
        print("student1 gender is :",self.gender)
    def student2_details(self):
        print("student2 name is:", self.name)
        print("student2 age is:",self.age)
        print("student2- current standard is:",self.standard)
        print("student2 total marks(out of 500)is:",self.total_marks)
        print("student2 grade is :",self.grade)
        print("student2 gender is :",self.gender)
    def student3_details(self):
        print("student3 name is:", self.name)
        print("student3 age is:",self.age)
        print("student3- current standard is:",self.standard)
        print("student3 total marks(out of 500)is:",self.total_marks)
        print("student3 grade is :",self.grade)
        print("student3 gender is :",self.gender)
    def student4_details(self):
        print("student4 name is:", self.name)
        print("student4 age is:",self.age)
        print("student4- current standard is:",self.standard)
        print("student4 total marks(out of 500)is:",self.total_marks)
        print("student4 grade is :",self.grade)
        print("student4 gender is :",self.gender)
    def student5_details(self):
        print("student5 name is:", self.name)
        print("student5 age is:",self.age)
        print("student5- current standard is:",self.standard)
        print("student5 total marks(out of 500)is:",self.total_marks)
        print("student5 grade is :",self.grade)
        print("student5 gender is :",self.gender)
print("CLASS_A_STUDENT_DETAILS:")
student1_classA=Class_A("Shivani",10,"5th standard",300,"C","Female")
student1_classA.student1_details()
student2_classA=Class_A("Harini",11,"5th standard",467,"B+","Female")
student2_classA.student2_details()
student3_classA=Class_A("Rahul",11,"5th standard",480,"A","Male")
student3_classA.student3_details()
student4_classA=Class_A("Rose",10,"5th standard",415,"B","Female")
student4_classA.student4_details()
student5_classA=Class_A("Kishore",11,"5th standard",498,"A+","Male")
student5_classA.student5_details()
class Class_B:
    def __init__(self, name, age, standard, total_marks, grade, gender):
        self.class_B=Class_A(name, age, standard, total_marks, grade, gender)
    def student1_classB(self):
        self.class_B.student1_details()
    def student2_classB(self):
        self.class_B.student2_details()
    def student3_classB(self):
        self.class_B.student3_details()
    def student4_classB(self):
        self.class_B.student4_details()
    def student5_classB(self):
        self.class_B.student5_details()
print("CLASS_B_STUDENT_DETAILS:")
student1_classB=Class_B("Raj",12,"5th standard",499,"A+","Male")
student1_classB.student1_classB()
student2_classB=Class_B("Jasmine",12,"5th standard",322,"C","Female")
student2_classB.student2_classB()
student3_classB=Class_B("Rakesh",11,"5th standard",491,"A+","Male")
student3_classB.student3_classB()
student4_classB=Class_B("Rithik",10,"5th standard",400,"B","Male")
student4_classB.student4_classB()
student5_classB=Class_B("Renu",12,"5th standard",460,"B+","Female")
student5_classB.student5_classB()










'''
"Python Learning"
Learning: "OOPS-concept-Polymorphism"
DAY01-Task

'''

'''
COMPILE TIME POLYMORPHISM
'''
print("==================COMPILE TIME POLYMORPHISM==============")
class calc:
    def calculation(self, a=1,b=2, *args):
        result = a * b
        for num in args:
            result *= num
        return result
calc_1=calc()
print(calc.calculation(1))

print(calc.calculation(7))

print(calc.calculation(10))

print(calc.calculation(11))

print(calc.calculation(3,2,6))

print(calc.calculation(20,10,1,2,3))
print()


'''
RUN-TIME POLYMORPHISM
'''
print("=================RUN-TIME POLYMORPHISM====================")
class Project1:
    def Emp_proj_details(self):
        return "consultant: Jasmine, project1: ACM-101, hours: 8 ,\nconsultant: Jane, project1: BET-5, hours: 9 ,\nconsultant: Barly, project1: ACM-102, hours: 6"

class Project2(Project1):
    def Emp_proj_details(self):
        return "consultant: Jasmine, project2: ACM-123, hours: 8 ,\nconsultant: Jane, project2: XCM-9, hours: 9 ,\nconsultant: Barly, project2: ACM-105, hours: 6"
class Project3(Project1):
    def Emp_proj_details(self):
        return "consultant: Jasmine, project3: ACM-193, hours: 8 ,\nconsultant: Jane, project3: XM-9, hours: 9 ,\nconsultant: Barly, project3: BET-105, hours: 6"
proj_1=[Project2(), Project1(), Project3()]
for projects in proj_1:
    print(projects.Emp_proj_details())
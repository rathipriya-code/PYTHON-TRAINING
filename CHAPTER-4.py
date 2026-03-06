'''
"Python Learning"
Learning: "OOPS-concept-Encapsulation"
DAY01-Task

'''

class Employee:
    def __init__(self,emp_name,annual_sal,tot_hours_per_week):
        self.name=emp_name
        self.salary=annual_sal
        self.hours_per_week=tot_hours_per_week
    def cal_hourly_rate(self):
        tot_annual_hours=self.hours_per_week*52
        hourly_rate=self.salary/tot_annual_hours
        return tot_annual_hours,round(hourly_rate, 2)

Values = Employee("Priya",100000.00,40)
tot_annual_hours,hourly_rate=Values.cal_hourly_rate()
print("EMPLOYEE DETAILS")
print()
print("EMPLOYEE NAME:",Values.name)
print()
print("EMPLOYEE ANNUAL SALARY:",Values.salary)
print()
print("EMPLOYEE WORKING HOURS PER WEEK:",Values.hours_per_week)
print()
print("TOTAL ANNUAL HOURS:",tot_annual_hours)
print()
print("HOURLY RATE:",hourly_rate)


     
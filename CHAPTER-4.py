'''
"Python Learning"
Learning: "OOPS-concept-Encapsulation with basic example"
DAY01-Task

'''

'''

public method


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
print("EMPLOYEE EXAMPLE:")
print()
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



'''
Encapsulation with Banking Example

"public", "protected", "private" - access modifiers in Python

'''

'''
public,private,protected method

'''

class BankAccount:
    def __init__(self):
        self.account_holder= "Priya"#here we using public variable
        self.__balance=10000.00 #here we using private variable
        self._mini_statement="1 Transactions yet on 2026-15-01 (With Deposit of RS.5,000)" #here we using protected variable
    def display_balance(self):
        print("\nAccount Holder:", self.account_holder)
        print("\nBalance: $", self.__balance)
    def update_balance(self, amount):
        self.__balance += amount
    def display_deposit_details(self,amount):
        if amount > 0:
            print("\nDeposit successful. New balance: $", self.__balance)
        else:
            print("\nInvalid deposit amount,check with Bank. Balance remains: $", self.__balance)
    def display_mini_statement(self):
        print("\nMini Statement: ", self._mini_statement)
print("============================================================================")
print("BANKING EXAMPLE:")
account = BankAccount()
account.display_balance()
account.update_balance(5000.00)
account.display_deposit_details(5000.00)
#print("\nAccount Holder name is:",account.account_holder)#we can access public method directly and outside the class 
#print(account.__balance)#but cant access private method directly, it throws Error
account.display_mini_statement()
#account.__balance=5678 #we can create a new attribute but it not cahnge the value of private method
#print("balance is:",account.__balance) #it will print the new attribute values
#print(account._mini_statement)#we can access protected method directly.
#account._mini_statement="transaction: deposit of $5000.00 on 2024-06-30" #we cant change the value of protected method directly 
#print(account._mini_statement)

'''

simple example- for public,private,protected method


'''

class BankAccount:
    def __init__(self):
        self.account_holder= "Priya"#here we using public variable
    def __display(self): #here we using private method
        self.balance=100000.00
        return self.balance
    def _display_mini_statement(self): #here we using protected method
        self.mini_statement="No transactions yet"
        return self.mini_statement
    def show_display(self):
        print("\nYour Balance is:",self.__display())
print("\n============================================================================")
print("SIMPLE EXAMPLE FOR PUBLIC,PRIVATE,PROTECTED METHOD:")
account = BankAccount()
print("\nAccount Holder name is:",account.account_holder)#we can access public directly outside the class
#account.__display()#we cant access private method directly, it throws Error
print("\nMini statement:",account._display_mini_statement())#we can access protected method directly outside the class
account.show_display()
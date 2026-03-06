'''
"Python Learning"
Learning: "OOPS-concept-Class,Object,method,function-with
 CAR PURCHASING EXAMPLE"
DAY01-Task

'''
class Customer_1:
    def __init__(self,total_price_cus1,tax_cus1,discount_cus1):
        self.total_price_cus1=total_price_cus1
        self.tax_cus1=tax_cus1
        self.discount_cus1=discount_cus1
    def discount_calculation1(self):
        self.discount_cal_cus1=(self.total_price_cus1*self.discount_cus1)/100
        self.total_price_after_discount_cus1=self.total_price_cus1 - self.discount_cal_cus1
    def tax_calculation1(self):
        self.tax_cal_cus1=(self.total_price_after_discount_cus1*self.tax_cus1)/100
    def total_car_price1(self):
        self.total_car_price_cus1=self.total_price_after_discount_cus1 + self.tax_cal_cus1
class Customer_2:
    def __init__(self,total_price_cus2,tax_cus2,discount_cus2):
        self.total_price_cus2=total_price_cus2
        self.tax_cus2=tax_cus2
        self.discount_cus2=discount_cus2
    def discount_calculation2(self):
        self.discount_cal_cus2=(self.total_price_cus2*self.discount_cus2)/100
        self.total_price_after_discount_cus2=self.total_price_cus2 - self.discount_cal_cus2
    def tax_calculation2(self):
        self.tax_cal_cus2=(self.total_price_after_discount_cus2*self.tax_cus2)/100
    def total_car_price2(self):
        self.total_car_price_cus2=self.total_price_after_discount_cus2 + self.tax_cal_cus2
class Customer_3:
    def __init__(self,total_price_cus3,tax_cus3,discount_cus3):
        self.total_price_cus3=total_price_cus3
        self.tax_cus3=tax_cus3
        self.discount_cus3=discount_cus3
    def discount_calculation3(self):
        self.discount_cal_cus3=(self.total_price_cus3*self.discount_cus3)/100
        self.total_price_after_discount_cus3=self.total_price_cus3 - self.discount_cal_cus3
    def tax_calculation3(self):
        self.tax_cal_cus3=(self.total_price_after_discount_cus3*self.tax_cus3)/100
    def total_car_price3(self):
        self.total_car_price_cus3=self.total_price_after_discount_cus3 + self.tax_cal_cus3
class Customer_4:
    def __init__(self,total_price_cus4,tax_cus4,discount_cus4):
        self.total_price_cus4=total_price_cus4
        self.tax_cus4=tax_cus4
        self.discount_cus4=discount_cus4
    def discount_calculation4(self):
        self.discount_cal_cus4=(self.total_price_cus4*self.discount_cus4)/100
        self.total_price_after_discount_cus4=self.total_price_cus4 - self.discount_cal_cus4
    def tax_calculation4(self):
        self.tax_cal_cus4=(self.total_price_after_discount_cus4*self.tax_cus4)/100
    def total_car_price4(self):
        self.total_car_price_cus4=self.total_price_after_discount_cus4 + self.tax_cal_cus4
class Customer_5:
    def __init__(self,total_price_cus5,tax_cus5,discount_cus5):
        self.total_price_cus5=total_price_cus5
        self.tax_cus5=tax_cus5
        self.discount_cus5=discount_cus5
    def discount_calculation5(self):
        self.discount_cal_cus5=(self.total_price_cus5*self.discount_cus5)/100
        self.total_price_after_discount_cus5=self.total_price_cus5 - self.discount_cal_cus5
    def tax_calculation5(self):
        self.tax_cal_cus5=(self.total_price_after_discount_cus5*self.tax_cus5)/100
    def total_car_price5(self):
        self.total_car_price_cus5=self.total_price_after_discount_cus5 + self.tax_cal_cus5
class Customer_6:
    def __init__(self,total_price_cus6,tax_cus6,discount_cus6):
        self.total_price_cus6=total_price_cus6
        self.tax_cus6=tax_cus6
        self.discount_cus6=discount_cus6
    def discount_calculation6(self):
        self.discount_cal_cus6=(self.total_price_cus6*self.discount_cus6)/100
        self.total_price_after_discount_cus6=self.total_price_cus6 - self.discount_cal_cus6
    def tax_calculation6(self):
        self.tax_cal_cus6=(self.total_price_after_discount_cus6*self.tax_cus6)/100
    def total_car_price6(self):
        self.total_car_price_cus6=self.total_price_after_discount_cus6 + self.tax_cal_cus6
cus1=Customer_1(500000,10,10)
cus1.discount_calculation1()
cus1.tax_calculation1()
cus1.total_car_price1()
print("CUSTOMER 1 PRICE DETAILS")
print("CUSTOMER 1 TOTAL PRICE FOR TOYOTA:",cus1.total_car_price_cus1)
cus2=Customer_2(800000,20,20)
cus2.discount_calculation2()
cus2.tax_calculation2()
cus2.total_car_price2()
print("CUSTOMER 2 PRICE DETAILS")
print("CUSTOMER 2 TOTAL PRICE FOR HYUNDAI:",cus2.total_car_price_cus2)
cus3=Customer_3(1000000,80,80)
cus3.discount_calculation3()
cus3.tax_calculation3()
cus3.total_car_price3()
print("CUSTOMER 3 PRICE DETAILS")
print("CUSTOMER 3 TOTAL PRICE FOR Maruti Suzuki:",cus3.total_car_price_cus3)
cus4=Customer_4(700000,30,30)
cus4.discount_calculation4()
cus4.tax_calculation4()
cus4.total_car_price4()
print("CUSTOMER 4 PRICE DETAILS")
print("CUSTOMER 4 TOTAL PRICE FOR Honda:",cus4.total_car_price_cus4)
cus5=Customer_5(1500000,40,40)
cus5.discount_calculation5()
cus5.tax_calculation5()
cus5.total_car_price5()
print("CUSTOMER 5 PRICE DETAILS")
print("CUSTOMER 5 TOTAL PRICE FOR Skoda:",cus5.total_car_price_cus5)
cus6=Customer_6(2000000,50,50)
cus6.discount_calculation6()
cus6.tax_calculation6()
cus6.total_car_price6()
print("CUSTOMER 6 PRICE DETAILS")
print("CUSTOMER 6 TOTAL PRICE FOR TOYOTA:",cus6.total_car_price_cus6)

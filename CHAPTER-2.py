'''
"Python Learning"
Learning: "OOPS-concept-Inheritance"
DAY01-Task

'''

'''
Single Inheritance

'''
class Cus_1:
    def Apartment_flat1(self):
        print("===================CUSTOMER_1============================")
        print("Priya bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def Apartment_flat2(self):
        print("Priya bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def Apartment_flat3(self):
        print("Priya bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Cus_2(Cus_1):
    def Apartment_flat4(self):
        print("===================CUSTOMER_2============================")
        print("Sreya bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def Apartment_flat5(self):
        print("Sreya bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def Apartment_flat6(self):
        print("Sreya bought 3-BHK-APARTMENT with price of RS.70,00,000")
Price_details=Cus_2()
Price_details.Apartment_flat1()
Price_details.Apartment_flat2()
Price_details.Apartment_flat3()
Price_details.Apartment_flat4()
Price_details.Apartment_flat5()
Price_details.Apartment_flat6()
print()
print("====================SINGLE INHERITANCE=====================")
print()


'''
Multiple Inheritance

'''
class Cus_1:
    def Apartment_flat1(self):
        print("===================CUSTOMER_1============================")
        print("Priya bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def Apartment_flat2(self):
        print("Priya bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def Apartment_flat3(self):
        print("Priya bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Cus_2():
    def Apartment_flat4(self):
        print("===================CUSTOMER_2============================")
        print("Sreya bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def Apartment_flat5(self):
        print("Sreya bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def Apartment_flat6(self):
        print("Sreya bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Cus_3(Cus_1,Cus_2):
    def Apartment_flat7(self):
        print("===================CUSTOMER_3============================")
        print("Bala bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def Apartment_flat8(self):
        print("Bala bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def Apartment_flat9(self):
        print("Bala bought 3-BHK-APARTMENT with price of RS.70,00,000")
Price_details=Cus_3()
Price_details.Apartment_flat1()
Price_details.Apartment_flat2()
Price_details.Apartment_flat3()
Price_details.Apartment_flat4()
Price_details.Apartment_flat5()
Price_details.Apartment_flat6()
Price_details.Apartment_flat7()
Price_details.Apartment_flat8()
Price_details.Apartment_flat9()
print()
print("===================MULTIPLE INHERITANCE========================")
print()

'''
Multilevel Inheritance

'''
class Cus_1:
    def Apartment_flat1(self):
        print("===================CUSTOMER_1============================")
        print("Priya bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def Apartment_flat2(self):
        print("Priya bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def Apartment_flat3(self):
        print("Priya bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Cus_2(Cus_1):
    def Apartment_flat4(self):
        print("===================CUSTOMER_2============================")
        print("Sreya bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def Apartment_flat5(self):
        print("Sreya bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def Apartment_flat6(self):
        print("Sreya bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Cus_3(Cus_2):
    def Apartment_flat7(self):
        print("===================CUSTOMER_3============================")
        print("Bala bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def Apartment_flat8(self):
        print("Bala bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def Apartment_flat9(self):
        print("Bala bought 3-BHK-APARTMENT with price of RS.70,00,000")
Price_details=Cus_3()
Price_details.Apartment_flat1()
Price_details.Apartment_flat2()
Price_details.Apartment_flat3()
Price_details.Apartment_flat4()
Price_details.Apartment_flat5()
Price_details.Apartment_flat6()
Price_details.Apartment_flat7()
Price_details.Apartment_flat8()
Price_details.Apartment_flat9()
print()
print("===================MULTILEVEL INHERITANCE========================")
print()

'''
Hierarchical Inheritance

'''
class Cus_1:
    def Apartment_flat1(self):
        print("===================CUSTOMER_1============================")
        print("Priya bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def Apartment_flat2(self):
        print("Priya bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def Apartment_flat3(self):
        print("Priya bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Cus_2(Cus_1):
    def Apartment_flat4(self):
        print("===================CUSTOMER_2============================")
        print("Sreya bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def Apartment_flat5(self):
        print("Sreya bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def Apartment_flat6(self):
        print("Sreya bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Cus_3(Cus_1):
    def Apartment_flat7(self):
        print("===================CUSTOMER_3============================")
        print("Bala bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def Apartment_flat8(self):
        print("Bala bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def Apartment_flat9(self):
        print("Bala bought 3-BHK-APARTMENT with price of RS.70,00,000")
Price_details_cus2=Cus_2()
Price_details_cus3=Cus_3()
Price_details_cus2.Apartment_flat1()
Price_details_cus2.Apartment_flat2()
Price_details_cus2.Apartment_flat3()
Price_details_cus2.Apartment_flat4()
Price_details_cus2.Apartment_flat5()
Price_details_cus2.Apartment_flat6()
Price_details_cus3.Apartment_flat7()
Price_details_cus3.Apartment_flat8()
Price_details_cus3.Apartment_flat9()
print()
print("=================HIERARCHICAL INHERITANCE======================")
print()

'''
Hybrid Inheritance

'''
class Cus_1:
    def Apartment_flat1(self):
        print("===================CUSTOMER_1============================")
        print("Priya bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def Apartment_flat2(self):
        print("Priya bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def Apartment_flat3(self):
        print("Priya bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Cus_2(Cus_1):
    def Apartment_flat4(self):
        print("===================CUSTOMER_2============================")
        print("Sreya bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def Apartment_flat5(self):
        print("Sreya bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def Apartment_flat6(self):
        print("Sreya bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Cus_3(Cus_2,Cus_1):
    def Apartment_flat7(self):
        print("===================CUSTOMER_3============================")
        print("Bala bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def Apartment_flat8(self):
        print("Bala bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def Apartment_flat9(self):
        print("Bala bought 3-BHK-APARTMENT with price of RS.70,00,000")
Price_details_cus3=Cus_3()
Price_details_cus3.Apartment_flat1()
Price_details_cus3.Apartment_flat2()
Price_details_cus3.Apartment_flat3()
Price_details_cus3.Apartment_flat4()
Price_details_cus3.Apartment_flat5()
Price_details_cus3.Apartment_flat6()
Price_details_cus3.Apartment_flat7()
Price_details_cus3.Apartment_flat8()
Price_details_cus3.Apartment_flat9()
print()
print("===================HYBRID INHERITANCE========================")
print()












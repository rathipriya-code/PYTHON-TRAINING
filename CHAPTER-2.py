'''

"Python Learning"
Learning: "OOPS-concept-Inheritance"


'''

'''
Single Inheritance

'''
class Apartment_1:
    def display_customer_1(self):
        print("===================APARTMENT_1============================")
        print("Priya bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def display_customer_2(self):
        print("sreya bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def display_customer_3(self):
        print("shivani bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Apartment_2(Apartment_1):
    def display_customer_4(self):
        print("===================APARTMENT_2============================")
        print("Harish bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def display_customer_5(self):
        print("Sayesha bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def display_customer_6(self):
        print("Sri bought 3-BHK-APARTMENT with price of RS.70,00,000")
Price_details=Apartment_2()
Price_details.display_customer_1()
Price_details.display_customer_2()
Price_details.display_customer_3()
Price_details.display_customer_4()
Price_details.display_customer_5()
Price_details.display_customer_6()
print()
print("====================SINGLE INHERITANCE=====================")
print()


'''
Multiple Inheritance

'''
class Apartment_1:
    def display_customer_1(self):
        print("===================APARTMENT_1============================")
        print("simbu bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def display_customer_2(self):
        print("Preethi bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def display_customer_3(self):
        print("Priya bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Apartment_2():
    def display_customer_4(self):
        print("===================APARTMENT_2============================")
        print("Anu bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def display_customer_5(self):
        print("Sreya bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def display_customer_6(self):
        print("Sri bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Apartment_3(Apartment_1,Apartment_2):
    def display_customer_7(self):
        print("===================APARTMENT_3============================")
        print("Gayatri bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def display_customer_8(self):
        print("Bala bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def display_customer_9(self):
        print("Bindhu bought 3-BHK-APARTMENT with price of RS.70,00,000")
Price_details=Apartment_3()
Price_details.display_customer_1()
Price_details.display_customer_2()
Price_details.display_customer_3()
Price_details.display_customer_4()
Price_details.display_customer_5()
Price_details.display_customer_6()
Price_details.display_customer_7()
Price_details.display_customer_8()
Price_details.display_customer_9()
print()
print("===================MULTIPLE INHERITANCE========================")
print()

'''
Multilevel Inheritance

'''
class Apartment_1:
    def display_customer_1(self):
        print("===================APARTMENT_1============================")
        print("Bindhu bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def display_customer_2(self):
        print("Preethi bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def display_customer_3(self):
        print("Priya bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Apartment_2(Apartment_1):
    def display_customer_4(self):
        print("===================APARTMENT_2============================")
        print("Sayesha bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def display_customer_5(self):
        print("Sri bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def display_customer_6(self):
        print("Sreya bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Apartment_3(Apartment_2):
    def display_customer_7(self):
        print("===================APARTMENT_3============================")
        print("pragan bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def display_customer_8(self):
        print("Bindhu bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def display_customer_9(self):
        print("Bala bought 3-BHK-APARTMENT with price of RS.70,00,000")
Price_details=Apartment_3()
Price_details.display_customer_1()
Price_details.display_customer_2()
Price_details.display_customer_3()
Price_details.display_customer_4()
Price_details.display_customer_5()
Price_details.display_customer_6()
Price_details.display_customer_7()
Price_details.display_customer_8()
Price_details.display_customer_9()
print()
print("===================MULTILEVEL INHERITANCE========================")
print()

'''
Hierarchical Inheritance

'''
class Apartment_1:
    def display_customer_1(self):
        print("===================APARTMENT_1============================")
        print("Preethi bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def display_customer_2(self):
        print("sreya bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def display_customer_3(self):
        print("Priya bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Apartment_2(Apartment_1):
    def display_customer_4(self):
        print("===================APARTMENT_2============================")
        print("Sri bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def display_customer_5(self):
        print("Sai bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def display_customer_6(self):
        print("Sreya bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Apartment_3(Apartment_1):
    def display_customer_7(self):
        print("===================APARTMENT_3============================")
        print("priya bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def display_customer_8(self):
        print("Bindhu bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def display_customer_9(self):
        print("Bala bought 3-BHK-APARTMENT with price of RS.70,00,000")
Price_details1=Apartment_2()
Price_details2=Apartment_3()
Price_details1.display_customer_1()
Price_details1.display_customer_2()
Price_details1.display_customer_3()
Price_details1.display_customer_4()
Price_details1.display_customer_5()
Price_details1.display_customer_6()
Price_details2.display_customer_7()
Price_details2.display_customer_8()
Price_details2.display_customer_9()
print()
print("=================HIERARCHICAL INHERITANCE======================")
print()

'''
Hybrid Inheritance

'''
class Apartment_1:
    def display_customer_1(self):
        print("===================APARTMENT_1============================")
        print("Priya bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def display_customer_2(self):
        print("Preethi bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def display_customer_3(self):
        print("sayesha bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Apartment_2(Apartment_1):
    def display_customer_4(self):
        print("===================APARTMENT_2============================")
        print("Sreya bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def display_customer_5(self):
        print("Sibin bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def display_customer_6(self):
        print("Sara bought 3-BHK-APARTMENT with price of RS.70,00,000")
class Apartment_3(Apartment_2,Apartment_1):
    def display_customer_7(self):
        print("===================APARTMENT_3============================")
        print("Bala bought 1-BHK-APARTMENT with price of RS.30,00,000")
    def display_customer_8(self):
        print("Bindhu bought 2-BHK-APARTMENT with price of RS.50,00,000")
    def display_customer_9(self):
        print("karthik bought 3-BHK-APARTMENT with price of RS.70,00,000")
Price_details=Apartment_3()
Price_details.display_customer_1()
Price_details.display_customer_2()
Price_details.display_customer_3()
Price_details.display_customer_4()
Price_details.display_customer_5()
Price_details.display_customer_6()
Price_details.display_customer_7()
Price_details.display_customer_8()
Price_details.display_customer_9()
print()
print("===================HYBRID INHERITANCE========================")
print()












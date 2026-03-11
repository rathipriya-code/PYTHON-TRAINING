'''
"Python Learning"
Learning: "OOPS-concept-Class,Object,method,function-with
 CAR PURCHASING EXAMPLE"


'''
class Car_customers:

    def __init__(self, name, car_brand, total_price, tax, discount):
        self.name = name
        self.car_brand = car_brand
        self.total_price = total_price
        self.tax = tax
        self.discount = discount

    def discount_calculation(self):
        self.discount_amount = (self.total_price * self.discount) / 100
        self.price_after_discount = self.total_price - self.discount_amount

    def tax_calculation(self):
        self.tax_amount = (self.price_after_discount * self.tax) / 100

    def total_price_calculation(self):
        self.final_price = self.price_after_discount + self.tax_amount

    def display_details(self):
        print("\nCustomer Name:", self.name)
        print("\nCar Brand:", self.car_brand)
        print("\nOriginal Price:", self.total_price)
        print("\nDiscount:", self.discount, "%")
        print("\nPrice After Discount:", self.price_after_discount)
        print("\nTax:", self.tax, "%")
        print("\nFinal Price:", self.final_price)



cus1 = Car_customers("Priya", "Toyota", 500000, 10, 10)
cus2 = Car_customers("Rahul", "Hyundai", 800000, 20, 20)
cus3 = Car_customers("Arun", "Maruti Suzuki", 1000000, 8, 5)
cus4 = Car_customers("Meena", "Honda", 700000, 12, 15)
cus5 = Car_customers("Kumar", "Skoda", 1500000, 18, 10)
cus6 = Car_customers("Anu", "Toyota", 2000000, 15, 12)

customers = [cus1, cus2, cus3, cus4, cus5, cus6]


for customer in customers:
    customer.discount_calculation()
    customer.tax_calculation()
    customer.total_price_calculation()
    customer.display_details()
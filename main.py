class Customer:
    def _init_(self, first_name, last_name, email, phone_number, addres, id):
        self.first_name = first_name
        self.last_name = last_name
        self.customer_email = email
        self.customer_number = phone_number
        self.customer_addres = addres
        self.customer_id = id
        self.__customer_balance = 0

    def display_info(self):
        print(f"Customer: {self.first_name} {self.last_name}. Phone number: {self.customer_number}. Email: {self.customer_email}. Addres: {self.customer_addres}. Id: {self.customer_id}.")

    def addOrders(self, amount):
        
        if(amount > 0):
            self.__customer_balance += amount
            print(f"New balance: {self.__customer_balance}")
        else:
            print("Nothing was changed")
    
    @staticmethod 
    def companyInfo():
        print("We are a company that will help you buy a car from America")

class Discount:
    def _init_(self, discount_rate):
        self.discount_rate = discount_rate

    def apply_discount(self, amount):
        return amount * (self.discount_rate - 1)
    
class RegularCustomer(Customer, Discount):
    def _init_(self, first_name, last_name, email, phone_number, addres, id, discount_rate):
        Customer._init_(self, first_name, last_name, email, phone_number, addres, id)
        Discount._init_(self, discount_rate)

    def get_discount_balance(self):
        print(f"Customer: {self.first_name} {self.last_name} have {self.discount_rate * 100}% dsicount")

class VIPCustomer(Customer):
    def _init_(self, first_name, last_name, email, phone_number, addres, id):
        super()._init_(self, first_name, last_name, email, phone_number, addres, id)
        self.vip_status = True

    def display_vip_status(self):
        print(f"Customer status {self.vip_status}")


if __name__ == "__main__":

    customer1 = Customer("Олег", "Бандрівський", "oleg@gmail.com", "098-765-4321", "Львів", 123)
    customer1.display_info()
    customer1.add_orders(500)
    Customer.company_info()
    

    regular_customer = RegularCustomer("Марія", "Іванова", "maria@gmail.com", "067-123-4567", "Київ", 456, 0.1)
    regular_customer.display_info()
    regular_customer.get_discount_balance()

    amount_with_discount = regular_customer.apply_discount(1000)
    print(f"Amount after discount: {amount_with_discount}")
    regular_customer.add_orders(amount_with_discount)
    
    vip_customer = VIPCustomer("Андрій", "Шевченко", "andriy@gmail.com", "050-987-6543", "Одеса", 789)
    vip_customer.display_info()
    vip_customer.display_vip_status()

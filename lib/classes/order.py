from classes.customer import Customer
from classes.coffee import Coffee

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        Order.all.append(self)

        coffee.orders(self)
        customer.coffees(coffee)

        customer.orders(self)
        # coffee.customers(customer)
        
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise Exception
        if not (1 <= value <= 10):
            raise Exception
        self._price = value

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise Exception
        self._customer = value
    
    @property 
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise Exception
        self._coffee = value

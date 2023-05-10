class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._customers = []

    @property
    def name(self):
        return self._name

    @property
    def orders(self):
        return self._orders

    @property
    def customers(self):
        return list(self._customers)

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise Exception
        self._name = value
        
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            if new_order.customer not in self._customers:
                self._customers.append(new_order.customer)
            self._orders.append(new_order)
        return self._orders
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer and isinstance(new_customer, Customer):
            self._customers.append(new_customer)
        return self._customers
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return None
        total_price = sum([order.price for order in self._orders])
        return total_price / len(self._orders)
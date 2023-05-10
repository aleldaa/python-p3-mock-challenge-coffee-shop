
class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._coffees = []

    @property
    def name(self):
        return self._name

    @property
    def orders(self):
        return self._orders

    @property
    def coffees(self):
        return list(set(self._coffees))

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception
        if not (1 <= len(value) <= 15):
            raise Exception
        self._name = value
        
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if new_coffee not in self._coffees and isinstance(new_coffee, Coffee):
            self._coffees.append(new_coffee)
        return self._coffees

    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        self._coffees.append(coffee)
        coffee.add_order(new_order)
        return new_order
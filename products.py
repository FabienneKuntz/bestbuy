class Product:
    def __init__(self, name, price, quantity):
        if name == "" or price < 0 or quantity < 0:
            raise ValueError("Please enter valid product name, price and quantity")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if quantity <= 0:
            self.active = False


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Quantity is greater than product quantity")

        total_price = quantity * self.price
        self.quantity = self.quantity - quantity

        if self.quantity <= 0:
            self.active = False

        return float(total_price)
        #return f"Total price: {total_price:.2f} €, New quantity: {self.quantity}"

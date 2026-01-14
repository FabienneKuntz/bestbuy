import products

class Store:
    def __init__(self, products):
        self.products = products


    def add_product(self, product):
        """Adds a product to the store"""
        self.products.append(product)


    def remove_product(self, product):
        """Removes a product from the store"""
        self.products.remove(product)


    def get_total_quantity(self):
        """Returns the total quantity of all items in the store"""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return int(total_quantity)


    def get_all_products(self):
        """Returns all products in the store"""
        all_products = []
        for product in self.products:
            if product.is_active() is True:
                all_products.append(product)
        return all_products


    def order(self, shopping_list):
        """Orders the products in the store and returns price of the order"""
        self.shopping_list = shopping_list
        full_price = 0
        for elem in self.shopping_list:
            product, quantity = elem
            full_price += product.buy(quantity)

        return float(full_price)


import products
import store

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)

def start(store):
    user_input = None
    print("   Store Menu")
    print("   ----------")
    while user_input != 4:
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        user_input = int(input("Please choose a number: "))
        print("------")


start(best_buy)





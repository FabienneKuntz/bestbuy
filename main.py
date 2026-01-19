import products
import store

def start(store):
    print("   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)

    while True:
        start(best_buy)
        user_input = input("Please choose a number: ")

        if user_input == "1":
            print("------")
            all_products = best_buy.get_all_products()
            for product in all_products:
                product.show()
            print("------\n")

        elif user_input == "2":
            total_quantity = store.Store.get_total_quantity(best_buy)
            print(f"Total of {total_quantity} items in store\n")

        elif user_input == "3":
            all_products = best_buy.get_all_products()
            counter = 1
            print("------")
            for product in all_products:
                print(f"{counter}. ", end="")
                product.show()
                counter += 1
            print("------")
            print("When you want to finish order, enter empty text.")
            while True:
                product_input = input("Which product # do you want? ")
                if product_input == "":
                    print("Thank you for shopping with us!\n")
                    break

                product_index = int(product_input) - 1

                if product_index < 0 or product_index >= len(all_products):
                    print("Invalid product number!\n")
                    continue

                amount_input = int(input("What amount do you want? "))

                try:
                    product_list[product_index].buy(amount_input)
                    print("Product added to list!\n")
                except ValueError:
                    print("Quantity larger than what exists\n")

        elif user_input == "4":
            break

        else:
            print("Error with your choice! Try again!\n")


if __name__ == "__main__":
    main()

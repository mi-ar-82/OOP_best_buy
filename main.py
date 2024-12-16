from products import Product

if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))  # Expected: 12500
    print(mac.buy(100))  # Expected: 145000
    print(mac.is_active())  # Expected: False

    print(bose.show())  # Expected: "Bose QuietComfort Earbuds, Price: 250, Quantity: 450"
    print(mac.show())  # Expected: "MacBook Air M2, Price: 1450, Quantity: 0"

    bose.set_quantity(1000)
    print(bose.show())  # Expected: "Bose QuietComfort Earbuds, Price: 250, Quantity: 1000"
    
    product_list = [products.Product("MacBook Air M2", price = 1450, quantity = 100),
                    products.Product("Bose QuietComfort Earbuds", price = 250, quantity = 500),
                    products.Product("Google Pixel 7", price = 500, quantity = 250),
                    ]
    
    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))
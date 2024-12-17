#from products import Product
import products
from store import Store

if __name__ == "__main__":
    #Create some products
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)
    pixel = products.Product("Google Pixel 7", price = 500, quantity = 250)

    print(bose.buy(50))  # Expected: 12500
    print(mac.buy(100))  # Expected: 145000
    print(mac.is_active())  # Expected: False

    print(bose.show())  # Expected: "Bose QuietComfort Earbuds, Price: 250, Quantity: 450"
    print(mac.show())  # Expected: "MacBook Air M2, Price: 1450, Quantity: 0"

    bose.set_quantity(1000)
    print(bose.show())  # Expected: "Bose QuietComfort Earbuds, Price: 250, Quantity: 1000"
    
    bose = products.Product("Bose QuietComfort Earbuds", price = 250, quantity = 500)
    mac = products.Product("MacBook Air M2", price = 1450, quantity = 100)
    
    store = Store([bose, mac])
    price = store.order([(bose, 5), (mac, 30), (bose, 10)])
    print(f"Order cost: {price} dollars.")
    
    
    
    
    # product_list = [products.Product("MacBook Air M2", price = 1450, quantity = 100),
    #                 products.Product("Bose QuietComfort Earbuds", price = 250, quantity = 500),
    #                 products.Product("Google Pixel 7", price = 500, quantity = 250),
    #                 ]
    #
    # store = Store(product_list)
    # products = store.get_all_products()
    # print(store.get_total_quantity())
    # print(store.order([(products[0], 1), (products[1], 2)]))
    
    
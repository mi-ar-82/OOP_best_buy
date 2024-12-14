class Product:
# Instance variables:
# Name (str)
# Price (float)
# Quantity (int)
# Active (bool)
    
    def __init__(self, name, price, quantity):
        # Validate inputs and raise exceptions if invalid
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        # Initialize instance variables
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True  # Product is active by default
    
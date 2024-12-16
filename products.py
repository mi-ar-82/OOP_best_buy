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
    
    def get_quantity(self):
        # get method for quantity
        return self.quantity


    def set_quantity(self, quantity: int):
        pass

    def is_active(self) -> bool:
        pass

    def activate(self):
        pass

    def deactivate(self):
        pass

    def show(self) -> str:
        pass

    def buy(self, quantity: int) -> float:
        pass

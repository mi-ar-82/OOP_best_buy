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
        #Set method for quantity. Deactivates the product if quantity reaches 0.
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        #checks if the product is active (boolean value)
        return self.active

    def activate(self):
        #activates product
        self.active = True

    def deactivate(self):
        # deactivates product
        self.active = False

    def show(self) -> str:
        #returns a string representation of the product
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        pass

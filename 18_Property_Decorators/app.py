class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    # Getter method
    @property
    def price(self):
        return self._price

    # Setter method with validation
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = new_price

    # Deleter method
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Create a Product object
product = Product(100)

# Access price
print("Initial Price:", product.price)

# Update price
product.price = 200
print("Updated Price:", product.price)

# Try setting a negative price
try:
    product.price = -50  # This will raise an error
except ValueError as e:
    print("Error:", e)

# Delete price
del product.price

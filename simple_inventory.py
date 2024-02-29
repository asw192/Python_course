class Product:
        
    inventory = []
    
    def __init__(self, name, price, quantity):
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
        Product.inventory.append(self)
    
    def display_info(self):
        print(f"Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}")
    
    def update_quantity(self, change):
        self.quantity += change
        operation = "added to" if change > 0 else "removed from"
        print(f"{abs(change)} units have been {operation} the inventory of {self.name}.")
    
    @classmethod
    def calculate_total_inventory_value(cls):
        total_value = sum(product.price * product.quantity for product in cls.inventory)
        return total_value

product1 = Product("Laptop", 1000, 10)
product2 = Product("Smartphone", 500, 20)

product1.display_info()
product2.display_info()

product1.update_quantity(-2)  
product2.update_quantity(5)   

total_inventory_value = Product.calculate_total_inventory_value()
print(f"Total inventory value: ${total_inventory_value}")

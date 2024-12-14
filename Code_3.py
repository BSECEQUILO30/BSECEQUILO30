class Product:
    def __init__(self, product_id, name, product_description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.product_description = product_description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}\nName: {self.name}\nDescription: {self.product_description}\nPrice: {self.price}\nQuantity: {self.quantity}"

def add_product(products):
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    product_description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    products.append(Product(product_id, name, product_description, price, quantity))
    print("Product added successfully!")

def update_stock_quantity(products):
    product_id = input("Enter product ID to update quantity: ")
    for product in products:
        if product.product_id == product_id:
            new_quantity = int(input("Enter new quantity: "))
            product.quantity = new_quantity
            print("Quantity updated successfully!")
            return
    print("Product not found.")

def display_products(products):
    if not products:
        print("No products in inventory.")
        return
    for product in products:
        print(product)

def calculate_total_value(products):
    total_value = 0
    for product in products:
        total_value += product.price * product.quantity
    print(f"Total value of inventory: {total_value}")

def main():
    products = []
    while True:
        print("\nInventory Management System:")
        print("1. Add product")
        print("2. Update stock quantity")
        print("3. Display all products")
        print("4. Calculate total value")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_product(products)
        elif choice == "2":
            update_stock_quantity(products)
        elif choice == "3":
            display_products(products)
        elif choice == "4":
            calculate_total_value(products)
        elif choice == "5":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

main()

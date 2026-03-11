from models import Customer, FoodItem, Menu, Transaction

customer = Customer("Josh")
burger = FoodItem("Spicy Burger", 10.99, "Main", 4.7)

menu = Menu()
menu.add_item(burger)

order = Transaction()
order.add_item(burger)

print(customer.name)
print(menu.items)
print(order.items)
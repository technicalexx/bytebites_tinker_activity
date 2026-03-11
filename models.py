## Initial Classes:

# ByteBites models
# Customer stores customer information and purchase history.
# FoodItem stores item details like name, price, category, and popularity.
# Menu stores a collection of FoodItem objects and supports filtering/sorting.
# Transaction stores selected items and calculates total cost.


# class Customer:
#     pass


# class FoodItem:
#     pass


# class Menu:
#     pass


# class Transaction:
#     pass


## Updated Classes:

# ByteBites models
# Customer stores customer information and purchase history.
# FoodItem stores item details like name, price, category, and popularity.
# Menu stores a collection of FoodItem objects and supports filtering/sorting.
# Transaction stores selected items and calculates total cost.


# class Customer:
#     def __init__(self, name):
#         self.name = name
#         self.purchase_history = []

#     def add_purchase(self, transaction):
#         self.purchase_history.append(transaction)


# class FoodItem:
#     def __init__(self, name, price, category, popularity_rating):
#         self.name = name
#         self.price = price
#         self.category = category
#         self.popularity_rating = popularity_rating

#     def __repr__(self):
#         return f"FoodItem({self.name}, {self.price}, {self.category}, {self.popularity_rating})"


# class Menu:
#     def __init__(self):
#         self.items = []

#     def add_item(self, food_item):
#         self.items.append(food_item)


# class Transaction:
#     def __init__(self):
#         self.items = []

#     def add_item(self, food_item):
#         self.items.append(food_item)


## New Updated Classes:

# ByteBites models
# Customer stores customer information and purchase history.
# FoodItem stores item details like name, price, category, and popularity.
# Menu stores a collection of FoodItem objects and supports filtering/sorting.
# Transaction stores selected items and calculates total cost.


# class Customer:
#     def __init__(self, name):
#         self.name = name
#         self.purchase_history = []

#     def add_purchase(self, transaction):
#         self.purchase_history.append(transaction)


# class FoodItem:
#     def __init__(self, name, price, category, popularity_rating):
#         self.name = name
#         self.price = price
#         self.category = category
#         self.popularity_rating = popularity_rating

#     def __repr__(self):
#         return f"FoodItem({self.name}, {self.price}, {self.category}, {self.popularity_rating})"


# class Menu:
#     def __init__(self):
#         self.items = []

#     def add_item(self, food_item):
#         self.items.append(food_item)

#     def filter_by_category(self, category):
#         pass

#     def sort_by_price(self):
#         pass

#     def sort_by_popularity(self):
#         pass


# class Transaction:
#     def __init__(self):
#         self.items = []

#     def add_item(self, food_item):
#         self.items.append(food_item)

#     def calculate_total(self):
#         pass


## Final Update for Classes:

# ByteBites models
# Customer stores customer information and purchase history.
# FoodItem stores item details like name, price, category, and popularity.
# Menu stores a collection of FoodItem objects and supports filtering/sorting.
# Transaction stores selected items and calculates total cost.


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_purchase(self, transaction):
        self.purchase_history.append(transaction)


class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def __repr__(self):
        return f"FoodItem({self.name}, {self.price}, {self.category}, {self.popularity_rating})"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, food_item):
        self.items.append(food_item)

    def filter_by_category(self, category):
        return [item for item in self.items if item.category.lower() == category.lower()]

    def sort_by_price(self):
        return sorted(self.items, key=lambda item: item.price)

    def sort_by_popularity(self):
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Transaction:
    def __init__(self):
        self.items = []

    def add_item(self, food_item):
        self.items.append(food_item)

    def calculate_total(self):
        return sum(item.price for item in self.items)
    

## Draft Testing here for now:

if __name__ == "__main__":
    burger = FoodItem("Spicy Burger", 10.99, "Main", 4.7)
    soda = FoodItem("Large Soda", 2.99, "Drinks", 4.2)
    cake = FoodItem("Chocolate Cake", 5.50, "Desserts", 4.8)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(cake)

    print("Drinks:", menu.filter_by_category("Drinks"))
    print("Sorted by price:", menu.sort_by_price())
    print("Sorted by popularity:", menu.sort_by_popularity())

    order = Transaction()
    order.add_item(burger)
    order.add_item(soda)

    print("Order total:", order.calculate_total())


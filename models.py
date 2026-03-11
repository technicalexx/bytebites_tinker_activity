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


class Transaction:
    def __init__(self):
        self.items = []

    def add_item(self, food_item):
        self.items.append(food_item)
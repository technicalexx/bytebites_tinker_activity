## Initial version:

<!-- # ByteBites UML Design

## Customer

- name: str
- purchase_history: list

## FoodItem

- name: str
- price: float
- category: str
- popularity_rating: float

## Menu

- items: list[FoodItem]
- filter_by_category(category)
- sort_by_price()
- sort_by_popularity()

## Transaction

- items: list[FoodItem]
- calculate_total()

---

Customer -> has purchase history
Menu -> contains many FoodItem objects
Transaction -> contains selected FoodItem objects -->

## Updated Version:

# ByteBites UML Design

## Overview

The ByteBites backend is designed around four core classes: Customer, FoodItem, Menu, and Transaction. These classes model the main objects described in the feature request and keep the design simple and focused.

## UML-Style Class Diagram

### Customer

Attributes:

- name: str
- purchase_history: list[Transaction]

Methods:

- add_purchase(transaction)

### FoodItem

Attributes:

- name: str
- price: float
- category: str
- popularity_rating: float

Methods:

- **repr**()

### Menu

Attributes:

- items: list[FoodItem]

Methods:

- add_item(food_item)
- filter_by_category(category)
- sort_by_price()
- sort_by_popularity()

### Transaction

Attributes:

- items: list[FoodItem]

Methods:

- add_item(food_item)
- calculate_total()

## Relationships

- A Menu contains many FoodItem objects.
- A Transaction contains selected FoodItem objects.
- A Customer has a purchase history made up of Transaction objects.

## Design Notes

- Customer stores a user's name and past transactions.
- FoodItem stores the basic data for a menu item.
- Menu manages the collection of all available items and supports filtering and sorting.
- Transaction groups selected items together and calculates the total cost.
- The design avoids extra classes or features not mentioned in the specification.

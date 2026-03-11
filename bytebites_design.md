# ByteBites UML Design

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
Transaction -> contains selected FoodItem objects

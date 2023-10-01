print("Welcome to the meal calculator!")
meal_cost = float(input("How much was the charge of the meal?: $"))
tip = 0.18 * meal_cost
sales_tax = .07 * meal_cost
total = meal_cost + tip + sales_tax
print(f"meal_cost: ${meal_cost:.2f}")
print(f"tip: ${tip:.2f}")
print(f"sales_tax: ${sales_tax:.2f}")
print(f"total: ${total:.2f}")








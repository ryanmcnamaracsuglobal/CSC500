print("Welcome to the meal calculator")

# Find Food Charge
meal = float(input("How much did your meal cost?: $"))

# 18 percent tip
tip_percentage = 18
tip_amount = (tip_percentage / 100) * meal

# 7 percent sales tax
sales_tax_percentage = 7
sales_tax_amount = (sales_tax_percentage / 100) * meal

# Total Price
total_price = meal + tip_amount + sales_tax_amount

# Display all output
print(f"Meal: ${meal:.2f}")
print(f"Tip ({tip_percentage}%): ${tip_amount:.2f}")
print(f"Sales Tax ({sales_tax_percentage}%): ${sales_tax_amount:.2f}")
print(f"Total Price: ${total_price:.2f}")






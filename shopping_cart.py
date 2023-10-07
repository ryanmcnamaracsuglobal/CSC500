# Creat ItemToPurchase class
class ItemToPurchase:
    def __init__(self):
        self.item_name = str('')
        self.item_price = float(0)
        self.item_quantity = int(0)

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_quantity * self.item_price:.2f}")

# Item 1 Calculations
item1 = ItemToPurchase()
item1.item_name = input('Enter item 1 name:\n')
item1.item_price = float(input('Enter item 1 price:\n'))
item1.item_quantity = int(input('Enter number of items:\n'))

# Item 2 Calculations
item2 = ItemToPurchase()
item2.item_name = input('Enter item 2 name:\n')
item2.item_price = float(input('Enter item 2 price:\n'))
item2.item_quantity = int(input('Enter number of items:\n'))

# Calculate total cost
total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

print('\nTOTAL COST')
item1.print_item_cost()
item2.print_item_cost()
print(f'Total: ${total_cost:.2f}')















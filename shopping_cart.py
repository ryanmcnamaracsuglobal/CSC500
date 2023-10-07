#Create Item to Purchase Class
class ItemToPurchase:
    def __init__(self):
        self.item_name = str('')
        self.item_price = float(0)
        self.item_quantity = int(0)

    def print_item_cost(self):
        print(self.item_name, end = ' ')
        print((self.item_quantity * self.item_price))

#Item 1 calculations
item1 = ItemToPurchase()
item1.item_name = str(input('Enter item 1 name:\n'))
item1.item_price = float(input('Enter item 1 price:\n'))
item1.item_quantity = int(input('Enter number of item:\n'))

#Item 2 calculations
item2 = ItemToPurchase()
item2.item_name = str(input('Enter item 2 name:\n'))
item2.item_price = float(input('Enter item 2 price:\n'))
item2.item_quantity = int(input('Enter number of item:\n'))

#Calculate Total Cost

total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print('TOTAL COST')
item1.print_item_cost()
item2.print_item_cost()
print('Total:', total_cost)












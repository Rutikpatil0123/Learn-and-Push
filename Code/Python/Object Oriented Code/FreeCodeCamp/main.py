import csv

class Item:
    
    pay_Rate = 0.8

    all = []

    def __init__(self, name : str, price : int, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def Calculate_total_price(self):
        return self.price * self.quantity

    def apply_Discount(self):
        self.price = self.price * self.pay_Rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = float(item.get('quantity'))

            )


    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"


# item1 = Item("Phone", 18000, 1)
# item1.apply_Discount()
# print(item1.Calculate_total_price())


# item2 = Item("Laptop", 75000, 2)
# item2.pay_Rate = 0.7
# item2.apply_Discount()
# print(item2.Calculate_total_price())

# print(Item.pay_Rate)
# print(item1.pay_Rate)

# print(Item.__dict__)
# print(item1.__dict__)

#print(Item.all)

Item.instantiate_from_csv()
print(Item.all)
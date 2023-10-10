class Phone:

    def __init__(self, ram_capacity, internal_Storage, Screen_Size, price):
        self.ram_capacity = ram_capacity
        self.internal_Storage = internal_Storage
        self.Screen_Size = Screen_Size
        self.price = price

    

Samsung = Phone("8", "128", "6.5", "20000")

print(Samsung.__dict__)


def count_properties(obj):
    properties = dir(obj)
    property_count = len([prop for prop in properties if not prop.startswith("__")])  # Exclude dunder methods
    
    print(f"Total number of properties in the class: {property_count}")

# Example usage:
class MyClass:
    def __init__(self):
        self.attribute1 = "value1"
        self.attribute2 = "value2"
        self._internal_attribute = "internal"

my_object = MyClass()

count_properties(my_object)  # This will print the total number of properties in the MyClass class

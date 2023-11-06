# This is tuple Inmutable
tup = ("ram", 5, 50.5, "Dham", True)
print(tup)

# This is list simliar to array
list = [4, 6, 2, "Sham", False, tup]
print(list)

#This is dict key Value pair

dict = {1 : "one", 2 : "Two", 3 : "Three", 4 : "Four"}
print(dict)

# To print all keys
con = dict.keys()
print(con)

for i in dict.items():
    print(i)

for i in dict.keys():
    print(i)

for i in dict.values():
    print(i)

greet = "Good Morning"
print(greet)

# This way we can traverse from last
print(tup[-2])

# Using for loop
for i in range(0,len(list)):
    print(list[i])

# Using for each loop
for i in list:
    print(i)

# slice list
print(tup[1:4])
sub_list = list[1:-1]
print(sub_list)
print(list[::-1])

# in is membership check operator
print(6 in list)

# append list
list + [0,1,2]
print(list)

# copy of same element
print(tup * 2)
print(tup)

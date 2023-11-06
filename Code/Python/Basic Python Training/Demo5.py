#String

greet = "Good Morning"

print(dir(greet))
greet.upper()
print(greet)

# join and split Strings
temp1 = ";".join(["abc","def","ghi"])
print(temp1)

temp2 = temp1.split(";")
print(temp2)

#Check plindrome
pal1 = "able was i ere i saw elba"
print((pal1 == pal1[::-1]))
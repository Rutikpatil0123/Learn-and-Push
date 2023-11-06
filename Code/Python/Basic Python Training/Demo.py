print("Hello World!")
print(3+5)

x = 34
y = 21.19
z = "fd"
print("x is", x)
print("y is", y)

if (x < 35):
    print("z is", z)
    y = y + 1 
    print(y)

print(y)

num1 = 10
num2 = 20

def swap(num1,num2):
    temp = num1
    num1 = num2
    num2 = temp
    print(num1,num2)

swap(num1,num2)
print(num1, num2)
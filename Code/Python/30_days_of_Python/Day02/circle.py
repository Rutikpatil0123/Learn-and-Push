PI = 3.14

def circumference_of_circle(radius):
    return 2 * PI * radius

def area_of_circle(radius):
    return 2 * PI * pow(radius,2)

def main():
    radius = float(input("Enter the radius of circle: "))

    print("Circumferencr of circle is ",circumference_of_circle(radius))
    print("area of circle is ",area_of_circle(radius))

if __name__ == "__main__":
    main()


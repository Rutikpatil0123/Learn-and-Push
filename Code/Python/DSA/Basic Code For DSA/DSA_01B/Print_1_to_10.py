def print_Numbers():
    start = int(input("Enter the start number : "))
    end = int(input("Enter the end number : "))

    for i in range(start, end):
        print(i)

def print_Even_Number():
    start = int(input("Enter the start number : "))
    end = int(input("Enter the end number : "))

    for i in range(start,end):
        if(i % 2 == 0):
            print(i)


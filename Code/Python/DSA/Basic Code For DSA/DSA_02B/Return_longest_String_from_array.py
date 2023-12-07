
def create_array():
    array = []
    array_size = int(input("Enter the size of array"))
    for i in range(0,array_size):
        temp = input("Input the ${i}th element of array")
        array.append(temp)

    return array

def print_longest_string(array):
    empty_string = "" 
    for i in range(0,len(array)):
        if(len(array[i])) > len(empty_string):
            empty_string = array[i]

    print(empty_string)

def main():
    array = create_array()
    print_longest_string(array)

if __name__ == '__main__':
    main()


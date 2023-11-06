
Array = []

def input_for_array(Array):
    array_Size = int(input("Enter the size of array: "))

    for i in range(0,array_Size):
        element = int(input(f'Enter the {i} element : '))
        Array.append(element)
    
    print(Array)
    print(len(Array))

def return_String_len():

    temp = str(input("Enter the String : "))
    print(temp)
    print(len(temp))



#input_for_array(Array)
return_String_len()
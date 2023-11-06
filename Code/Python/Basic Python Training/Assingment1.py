# delete the dulpicate and preserve order

def delete_duplicate_ele():
    li1 = [11,12,54,62,12,35,31]
    li2 = []

    for i in li1:
        if(li2.count(i) == 0):
            li2.append(i)

    print(li2)

#delete_duplicate_ele()

# Input key print value

def Input_key_Print_Value():
    dict = {1 : "Rutik", 2 : "Ram", 3 : "Sham"}

    key = int(input("Enter the key : "))

    if key in dict:
        print(dict[key])
    else:
        print("Enter a valid key")

    print(dict(dir))

#Input_key_Print_Value()


# Input value and print all corresponding keys

def Print_all_keys_for_input_key():
     dict = {1 : "Rutik", 2 : "Ram", 3 : "Sham"}

     temp = input("Enter your value : ")

     list = dict.items()

     for i, j in list:
        if j == temp:
            print(i)

Print_all_keys_for_input_key()
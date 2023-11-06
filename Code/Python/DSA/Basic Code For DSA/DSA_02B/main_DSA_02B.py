class DSA_02B:

    list = []

    def Check_Even_Odd(self):
        number = int(input("Enter your number : "))

        if(number % 2 == 0):
            return True
        else :
            return False

    def Check_String(self, temp = "temp"):
        return True

    def Check_Array_is_Empty(self):

        list = [2,82,6,1,5]

        if(len(list) > 0):
            return True
        else : 
            return False

    def Input_Array(self):

        Array = []

        array_size = int(input("Enter the size of array : "))

        for i in range(0,array_size):
            temp = str(input(f"Enter the {i} String : "))
            Array.append(temp)

        return Array

    def Capitalize_Strings_Of_Array(self, array):
        print(array)
        new_String_Array = [i.capitalize for i in array]
        print(new_String_Array)
        

    def Modify_Array(self,array):

        result_array = [i * 2 for i in array]
        print(result_array)
    







code = DSA_02B()
#print(code.Check_Even_Odd())
#print(code.Check_Array_is_Empty())
abc = code.Input_Array()
code.Capitalize_Strings_Of_Array(abc)
#code.Modify_Array(abc)
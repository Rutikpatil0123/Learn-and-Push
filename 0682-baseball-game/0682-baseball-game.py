class Solution(object):
    def calculate(list):
        
        result = 0
        
        for i in list:
            result = result + i
            
        return result
    
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        list = []
        
        for i in operations:
            if i == "+":
                val = list[-1] + list[-2]
                list.append(val)
            elif i == "D":
                val = list[-1] * 2
                list.append(val)
                
            elif i == "C":
                list.pop()
                
            else:
                list.append(int(i))
        print(list)       
        result = 0       
        for i in list:
            result = result + i
            
        return result
                
        
                
        
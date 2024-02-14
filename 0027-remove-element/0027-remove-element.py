class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        j = len(nums)-1
        ans = 0
        i = 0
        while i <= j:
            
            if(nums[i] == val):
                nums[i] = nums[j]
                nums[j] = val
                j = j - 1
            else:
                i = i + 1 
            ans = i
            
        return ans
                
            
        
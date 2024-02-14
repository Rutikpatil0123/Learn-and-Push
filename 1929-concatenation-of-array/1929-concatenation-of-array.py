class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list = []
        for i in range(0,len(nums)):
            list.insert(i,nums[i])
            
        for i in range(0,len(nums)):
            list.insert(i+len(nums),nums[i])
            
        return list
        
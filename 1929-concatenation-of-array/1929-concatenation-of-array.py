class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import copy
        list = copy.deepcopy(nums)
        for i in range(0,len(nums)):
            list.append(nums[i])

            
        return list
        
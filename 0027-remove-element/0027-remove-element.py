class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        list_size = len(nums)
        for index in range(list_size):
            if nums[index] != val:
                nums[i] = nums[index]
                i = i + 1
        
        return i 
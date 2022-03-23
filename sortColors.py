class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        teste=nums
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i]<teste[j]):
                    val= nums[i]
                    nums[i] = nums[j]
                    nums[j] = val
                # j=j+1
        print(nums)
            
#esse consegui sozinha
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
     
        i=0
        while ( i<len(nums)):
            if(nums[i]==target):
                return i
            i = i+1
        return -1
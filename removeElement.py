class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        print(val)
        i=0
        k=0
        while(i< len(nums)):
            print(nums[i])
            if(val != nums[i]):
                # del(nums[i])
                # nums[i]= "_"
                nums[k] = nums[i]
        
                k=k+1

            i=i+1
        print(nums)
        print(k)

        #correto
        class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0
        for i in range(len(nums)):
            if(nums[i]!=val):
                nums[k]=nums[i]
                k=k+1
        return k
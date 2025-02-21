class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in nums:
            while val in nums:
                nums.remove(val)
        return len(nums)

  #This solution uses 0s of runtime 
  #You must use a while loop, not a for loop as for loop will cause the string to "shift" left

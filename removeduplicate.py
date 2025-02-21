class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        #myset = set(nums)

        """
        for i in nums:
            if i not in seen:
                nums2.append(i)
                seen.append(i)
        nums[:] = nums2
        return len(nums)

        """
    
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]: #need to check behind first
                nums[j] = nums[i]
                j +=1
        return j

        #This solution uses the two pointer method to check if duplicate exists later in string

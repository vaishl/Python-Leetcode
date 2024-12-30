class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        
        this solution has o (n^2) time complexity, quite bad. i will now solve with dictionary 
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        '''
        sum = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in sum:
                return [sum[complement], i]

            sum[num] = i


solution = Solution()
result = solution.twoSum([2,3,4,5,6], 6)
print(result)
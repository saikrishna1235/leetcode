class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def solve(arr):
            n = len(arr)
            
            prev2 = 0
            prev1 = 0
            
            for i in range(n):
                take = arr[i] + prev2
                not_take = prev1
                
                curr = max(take, not_take)
                
                prev2 = prev1
                prev1 = curr
                
            return prev1
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        return max(solve(nums[:-1]), solve(nums[1:]))

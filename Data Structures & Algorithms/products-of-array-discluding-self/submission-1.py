class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        prefix = [1] * n
        suffix = [1] * n
        # loop 1: fill prefix, left to right
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums [i-1]
    
        # loop 2: fill suffix, right to left
        for j in range(n-2,-1,-1):
            suffix[j] = suffix[j+1] * nums [j+1]
        # loop 3: combine
        for k in range(n):
            ans[k] = prefix[k] * suffix[k]
        
        return ans
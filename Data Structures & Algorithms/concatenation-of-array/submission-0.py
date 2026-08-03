class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        ans = [0] * (2 * arr_len)
        for i, num in enumerate(nums):
            ans[i] = num
            ans[i+arr_len] = num
        return ans
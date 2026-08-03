class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums += nums
        ans = nums
        return ans
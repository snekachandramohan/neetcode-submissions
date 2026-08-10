class Solution:
    def sortColors(self, nums: List[int]) -> None:
        from collections import Counter
        count = Counter(nums)
        nums[:] = [0]*count[0] + [1]*count[1] + [2]*count[2]
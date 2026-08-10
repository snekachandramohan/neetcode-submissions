class Solution:
    def sortColors(self, nums: List[int]) -> None:
        from collections import Counter
        count = Counter(nums)
        i = 0
        for color in range(3):
            nums[i:i+count[color]] = [color] * count[color]
            i += count[color]
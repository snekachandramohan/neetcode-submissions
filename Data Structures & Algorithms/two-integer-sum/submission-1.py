class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in cache:
                return [cache[rest], i]
            cache[nums[i]] = i
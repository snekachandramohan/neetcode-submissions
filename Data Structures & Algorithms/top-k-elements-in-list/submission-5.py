from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums).most_common(k)
        res = []
        for key, count in counter:
                res.append(key)
        return res
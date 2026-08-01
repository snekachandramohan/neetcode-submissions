from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        # Create buckets indexed by frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counter.items():
            buckets[count].append(num)
        
        # Collect top k from highest frequency buckets
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            res.extend(buckets[i])
            if len(res) >= k:
                return res[:k]
        
        return res
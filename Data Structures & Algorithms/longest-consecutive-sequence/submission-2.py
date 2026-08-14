class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  
            #  pass through each item, if an item has number less than that, increase count, if not ignore that number. 
            cset = set(nums)
            longest = 0
            for num in cset:
                if num - 1 not in cset:
                    current = num
                    length = 1
                    while current + 1 in cset:
                        current+=1
                        length+=1
                    longest = max(longest, length)
            return longest
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for word in strs:
            fsc = frozenset(Counter(word).items())
            hmap[fsc].append(word)
        return list(hmap.values())

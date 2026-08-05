class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs = sorted(strs)
        len_first = len(strs[0])
        len_last = len(strs[-1])
        for i in range(min(len_first, len_last)):
            if strs[0][i] != strs [-1][i]:
                return res
            else:
                res += strs[0][i]
        return res
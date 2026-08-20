class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        ans = []
        while i < j:
            if target < numbers[i] + numbers[j]:
                j-=1
            elif target > numbers[i] + numbers[j]:
                i+=1
            elif target == numbers[i] + numbers[j]:
                ans.append(i+1)
                ans.append(j+1)
                return ans



        
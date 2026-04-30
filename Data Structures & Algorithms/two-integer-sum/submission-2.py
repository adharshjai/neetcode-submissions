class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        firstMap = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in firstMap:
                return [firstMap[difference], i]
            firstMap[n] = i

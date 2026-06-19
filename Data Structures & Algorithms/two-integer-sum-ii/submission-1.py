class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numsMap = {}

        for i, n in enumerate(numbers, start=1):
            diff = target - n
            if diff in numsMap:
                return [numsMap[diff], i]
            numsMap[n] = i
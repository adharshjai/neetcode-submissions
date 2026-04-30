class Solution:
    def search(self, nums: List[int], target: int) -> int:
        numsMap = {}
        for i, n in enumerate(nums):
            numsMap[n] = i
            if target in numsMap:
                return i
        return -1
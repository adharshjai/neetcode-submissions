class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupMap = {}

        for i, n in enumerate(nums):
            if n in dupMap:
                return True
            dupMap[n] = i

        return False
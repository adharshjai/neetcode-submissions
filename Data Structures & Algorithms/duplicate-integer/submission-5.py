class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsMap = {}

        for i,n in enumerate(nums):
            if n in numsMap:
                return True
            numsMap[n] = i

        
        return False
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        

        for i, n in enumerate(nums):
            numsum = 1
            array = []
            for c in nums:
                array.append(c)
            array.pop(i)
            for s in array:
                numsum *= s
            output.append(numsum)
        
        return output
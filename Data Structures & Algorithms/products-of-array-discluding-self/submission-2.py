class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l=list(nums)
        for i in range(len(nums)):
            p=1
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    p*=nums[j]
            l[i]=p
        return l
        
                    
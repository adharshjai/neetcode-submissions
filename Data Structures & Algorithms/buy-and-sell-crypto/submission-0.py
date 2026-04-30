class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            val = prices[i]
            for j in range(i+1, len(prices)):
                prof = prices[j]
                res = max(res, prof - val)
        
        return res


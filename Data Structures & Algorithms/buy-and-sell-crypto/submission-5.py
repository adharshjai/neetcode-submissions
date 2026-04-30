class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        buy = prices[0]
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                if diff > profit:
                    profit = diff
            else:
                l = r
            r += 1
        
        return profit


                


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        total = 0
        buying = prices[0]
        while r < len(prices):
            if prices[r] - prices[l] > total:
                total = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
            r += 1
        return total
            
            
                
            

            

        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Keep track of the selling, buying, and total profit
        #Iterate through prices
        #If the current is higher than the selling, subtract the buying from current and take the profit
        #If the current is lower than the buying: How to know when to move the window over?
        minbuy = prices[0]
        total = 0
        for i in range(len(prices)):
            if (prices[i] - minbuy) > total:
                total = prices[i] - minbuy
            if minbuy > prices[i]:
                minbuy = prices[i]
        return total
            
            
                
            

            

        
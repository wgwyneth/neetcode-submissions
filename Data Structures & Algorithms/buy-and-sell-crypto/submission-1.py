class Solution:
    '''BruteForce Version with o(n^2)'''
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        bestBuy = -1
        bestSell = -1

        for potentialBuy in range(len(prices)):
            for potentialSell in range(potentialBuy, len(prices)):
                potentialProfit = prices[potentialSell] - prices[potentialBuy]
                if potentialProfit > maxProfit:
                    maxProfit = potentialProfit
                
        return maxProfit

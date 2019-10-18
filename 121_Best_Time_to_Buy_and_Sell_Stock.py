class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        minbuy = max(prices)
        maxprofit = 0
        
        for i in range(n):
            if prices[i]<minbuy:
                minbuy=prices[i]
            if prices[i]-minbuy>maxprofit:
                maxprofit=prices[i]-minbuy
            
        return maxprofit
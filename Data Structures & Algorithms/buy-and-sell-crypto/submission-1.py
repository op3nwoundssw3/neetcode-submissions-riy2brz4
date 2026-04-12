class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maximus = 0
        while r<=len(prices) - 1:
            profit = prices[r] - prices[l]
            maximus = max(profit,maximus)
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1
        return maximus

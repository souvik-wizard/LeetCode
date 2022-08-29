class Solution:
    def maxProfit(self, prices: List[int]) -> int:
                buy=0
                sell=1
                profit=0

                while sell<len(prices):
                    profit=max(profit,prices[sell]-prices[buy])
                    if prices[sell]-prices[buy] < 0:
                        buy=sell
                        print(buy)
                    sell+=1
                return profit
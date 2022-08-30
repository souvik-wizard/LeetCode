class Solution:
    def maxProfit(self, prices: List[int]) -> int:
                buy,sell,profit=0,1,0
                # Why sell=1?
                # why run while loop one time extra for no reason.
                while sell<len(prices):
                    profit=max(profit,prices[sell]-prices[buy])
                    if prices[sell]-prices[buy] < 0:
                        buy=sell
                        print(buy)
                    sell+=1
                return profit
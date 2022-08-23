class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res=numBottles
        while numBottles>=numExchange:
            rem=numBottles%numExchange
            numBottles//=numExchange
            res+= numBottles
            numBottles+=rem
        return res
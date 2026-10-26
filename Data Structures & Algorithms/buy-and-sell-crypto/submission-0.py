class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        k = 1
        for i in prices:
            for j in prices[k:]:
                _p = j-i
                if _p > p:
                    p = _p
            k += 1
        return p

            
        
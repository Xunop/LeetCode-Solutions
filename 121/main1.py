# Time Limit Exceeded
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)):
            if i == len(prices) - 1:
                break
            m = max(prices[i+1:])
            ans = max(m - prices[i] if m > prices[i] else 0, ans)
        return ans

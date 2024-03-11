class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i] is the max profit at day i
        dp = [0] * len(prices)
        m = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - m)
            m = min(m, prices[i])
        return dp[len(prices) - 1]

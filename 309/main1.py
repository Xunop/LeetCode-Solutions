class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # df[i][0]: 表示第 i 天结束时，手上持有股票的最大收益
        # df[i][1]: 表示第 i 天结束时，不持有股票，并且明天不可以购买股票的最大收益
        # df[i][2]: 表示第 i 天结束时，不持有股票，并且明天可以购买股票的最大收益
        
        n = len(prices)
        df = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        for i in range(1, n):
            # df[i][0] 由 df[i - 1][0] 和 df[i - 1][2] - prices[i] 转移而来
            # i - 1 天手上持有股票或者 i - 1 天结束时不持有股票，并且明天可以购买股票
            df[i][0] = max(df[i - 1][0], df[i - 1][2] - prices[i])
            # df[i][1] 由 df[i - 1][0] + prices[i] 转移而来
            # i - 1 天手上持有股票，第 i 天卖出
            df[i][1] = df[i - 1][0] + prices[i]
            # df[i][2] 由 df[i - 1][1] 和 df[i - 1][2] 转移而来
            # i - 1 天结束时不持有股票，并且明天不可以购买股票或者 i - 1 天结束时不持有股票，并且明天可以购买股票
            df[i][2] = max(df[i - 1][1], df[i - 1][2])
        return max(df[n - 1][1], df[n - 1][2])

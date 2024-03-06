class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for t in range(len(temperatures)):
            # Stack not emoty and current temperature > temperature at index in stack
            while stack and temperatures[t] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = t - index + 1
            stack.append(t)
        return ans

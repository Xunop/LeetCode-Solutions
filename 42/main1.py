class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0
        for i in range(len(height)):
            j = i + 1
            while j < len(height) and height[j] <= height[i]:
                rain += height[i] - height[j]
                j += 1
            i = j
        return rain

class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0
        i = 0
        while (i < len(height)):
            j = i + 1
            while j < len(height) and height[j] <= height[i]:
                j += 1
            if j == i + 1:
                i += 1
                continue
            elif j == len(height) - 1 and height[j] < height[i]:
                i += 1
                continue
            elif j != i + 1 and j < len(height) - 1:
                i += 1
                continue
            else:
                print('i = ', i, 'j = ', j, 'rain = ', rain)
                for k in range(i + 1, j):
                    rain += height[i] - height[k]
                i = j
                print('rain = ', rain)
        return rain

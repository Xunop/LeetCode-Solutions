class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        rain = 0
        leftMax, rightMax = height[left], height[right]
        left += 1
        right -= 1
        while (left <= right):
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax < rightMax:
                rain += leftMax - height[left]
                left += 1
            else:
                rain += rightMax - height[right]
                right -= 1
        return rain

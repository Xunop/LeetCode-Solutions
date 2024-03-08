class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        # Key is num in nums2, val is greater number
        d = {}
        for num in nums2:
            while stack and num > stack[-1]:
                d[stack.pop()] = num
            stack.append(num)
        return [d.get(num, -1) for num in nums1]

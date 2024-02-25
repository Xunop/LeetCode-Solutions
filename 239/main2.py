class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []

        deque_index = deque()

        res = []

        for i in range(len(nums)):
            while deque_index and deque_index[0] < i - k + 1:
                deque_index.leftpop()
            while deque_index and nums[deque_index[-1]] < nums[i]:
                deque_index.pop()
            deque_index.append(i)
            if i >= k - 1:
                

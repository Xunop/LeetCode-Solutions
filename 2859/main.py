class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum = 0
        arr = []
        for i in range(len(nums)):
            n = bin(i)
            count = 0
            while n:
                count += n & 1
                n >>= 1
            if count == k:
                arr.append(i)
        for i in arr:
            sum += nums[i]
        return sum

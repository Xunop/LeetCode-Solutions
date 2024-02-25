class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, prefixSum = 0, 0
        prefixSumCount = {0: 1}
        for num in nums:
            if prefixSum + num - k in prefixSumCount:
                count += prefixSumCount[prefixSum + num - k]
            prefixSum += num
            prefixSumCount[prefixSum] = prefixSumCount.get(prefixSum, 0) + 1
        return count
        

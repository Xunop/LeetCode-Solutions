class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        sum = 1
        zero = 0
        for num in nums:
            if num == 0:
                zero += 1
                continue
            sum *= num
        if zero > 1:
            return [0] * len(nums)
        else:
            for num in nums:
                if zero > 0:
                    res.append(0 if num != 0 else sum)
                else:
                    res.append(sum // num)
        return res

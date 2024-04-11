class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = map(str, nums)
        # Compare two strings by concatenating them in different order
        # then can get tha answer
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1
        strs = sorted(strs, key=functools.cmp_to_key(cmp), reverse=True)
        return ''.join(strs) if strs[0] != '0' else '0'

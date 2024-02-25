class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_dict = {}
        max_len = 1
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)

                hash_dict[num] = 1

                cur_len = left + right + 1

                max_len = max(cur_len, max_len)

                hash_dict[num] = cur_len
                hash_dict[num - left] = cur_len
                hash_dict[num + right] = cur_len
        return max_len

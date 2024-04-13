class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        # 1. n is even, n = n / 2
        # 2. n is odd, having following two cases:
        #    2.1 If the last two digits of `n` are '11', then adding 1 will cause the last two digits of n to become '00', which can make n become an even number faster.
        #    2.2 If the last two digits of `n` are '01', then subtracting 1 will cause the last two digits of n to become '00', which can make n become an even number faster.
        while n != 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or ((n >> 1) & 1) == 0:
                n -= 1
            else:
                n += 1
            count += 1
        return count

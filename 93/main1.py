class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path):
            if len(path) == 4:
                # print(path)
                if start == len(s):
                    res.append('.'.join(path))
                return
            for i in range(start, min(start + 3, len(s))):
                # Prevent leading 0
                if i > start and s[start] == '0':
                    break
                num = int(s[start:i + 1])
                if num < 256:
                    backtrack(i + 1, path + [s[start:i + 1]])
        res = []
        backtrack(0, [])
        return res

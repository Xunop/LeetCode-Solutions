class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1, arr2 = version1.split('.'), version2.split('.')

        n, m = len(arr1), len(arr2)
        i, j = 0, 0
        while i < n or j < m:
            a, b = 0, 0
            if i < n:
                a = int(arr1[i])
                i += 1
            if j < m:
                b = int(arr2[j])
                j += 1
            if a != b:
                return 1 if a > b else -1
        return 0

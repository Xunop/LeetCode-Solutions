class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = intervals.copy()
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i == j: continue
                if intervals[j][0] >= intervals[i][0] and intervals[j][0] <= intervals[i][1]:
                    temp = [intervals[i][0], max(intervals[i][1], intervals[j][1])]
                    res.remove(intervals[i])
                    res.remove(intervals[j])
                    res.append(temp)
        return res

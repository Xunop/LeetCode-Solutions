class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = collections.defaultdict(list)
        indigree = [0] * numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indigree[info[0]] += 1

        queue = collections.deque([u for u in range(numCourses) if indigree[u] == 0])
        
        res = []
        
        while queue:
            course = queue.popleft()
            res.append(course)
            for i in edges[course]:
                indigree[i] -= 1
                if indigree[i] == 0:
                    queue.append(i)
        return res if len(res) == numCourses else []

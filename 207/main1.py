class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        # Get the indegree and adjacency of every course.
        for info in prerequisites:
            # info[1] -> info[0]
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        queue = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0

        while queue:
            visited += 1
            # Get the node with 0 indegree.
            course = queue.popleft()
            for i in edges[course]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    queue.append(i)
        return visited == numCourses

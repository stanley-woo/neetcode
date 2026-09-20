class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        graph = defaultdict(list)
        in_degrees = defaultdict(int)

        for u, v in relations:
            graph[u].append(v)
            in_degrees[v] += 1
        
        queue = deque()
        for i in range(1, n + 1):
            if in_degrees[i] == 0:
                queue.append(i)

        res, lessons_taken = 0, 0
        while queue:
            size = len(queue)
            res += 1
            for _ in range(size):
                cur_course = queue.popleft()
                lessons_taken += 1
                for course in graph[cur_course]:
                    in_degrees[course] -= 1
                    if in_degrees[course] == 0:
                        queue.append(course)
        if lessons_taken != n:
            return -1
        return res 
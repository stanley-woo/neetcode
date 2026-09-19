class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = defaultdict(list)
        
        for i in range(len(pid)):
            process, parent = pid[i], ppid[i]

            if parent == 0:
                continue
            else:
                graph[parent].append(process)
        
        queue = deque()
        visited = set()
        queue.append(kill)
        visited.add(kill)

        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for child in graph[curr]:
                if child not in visited:
                    queue.append(child)
        
        return res
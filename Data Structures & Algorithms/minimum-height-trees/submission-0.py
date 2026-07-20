class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj_list = defaultdict(list)
        degree = [0] * n

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        
        nodes_left = n
        while nodes_left > 2:
            leaves = len(queue)
            nodes_left -= leaves
            for _ in range(leaves):
                node = queue.popleft()
                for nei in adj_list[node]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        queue.append(nei)
        return list(queue)
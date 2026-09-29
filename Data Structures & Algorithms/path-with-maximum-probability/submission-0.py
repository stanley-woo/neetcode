class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        pq = [(-1.0, start_node)]
        visited = set()
        while pq:
            curr_prob, curr_node = heapq.heappop(pq)
            visited.add(curr_node)
            if curr_node == end_node:
                return -curr_prob
            
            for nei, prob in graph[curr_node]:
                if nei not in visited:
                    heapq.heappush(pq, (curr_prob * prob, nei))
        return 0
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hash_map_in = defaultdict(list)
        hash_map_out = defaultdict(list)
        for u, v in trust:
            hash_map_in[v].append(u)
            hash_map_out[u].append(v)
        
        for i in range(n+1):
            if len(hash_map_in[i]) == n - 1 and len(hash_map_out[i]) == 0:
                return i
        
        return -1
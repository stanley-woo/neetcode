class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self, person):
        if self.parents[person] != person:
            self.parents[person] = self.find(self.parents[person])
        
        return self.parents[person]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
        
        if self.rank[root_a] > self.rank[root_b]:
            self.parents[root_b] = root_a
        elif self.parents[root_a] < self.rank[root_b]:
            self.parents[root_a] = root_b
        else:
            self.parents[root_b] = root_a
            self.rank[root_a] += 1
        
        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x: x[0])
        uf = UnionFind(n)
        group_cnt = n

        for timestamp, a, b in logs:
            if uf.union(a,b):
                group_cnt -= 1
            
            if group_cnt == 1:
                return timestamp
        
        return -1
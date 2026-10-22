class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1
            return True
        return False

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        uf = UnionFind(n)

        sorted_pairs = sorted((num, i) for i, num in enumerate(nums))

        for i in range(1, n):
            if sorted_pairs[i][0] - sorted_pairs[i-1][0] <= limit:
                uf.union(sorted_pairs[i][1], sorted_pairs[i-1][1])
        
        component_indices = defaultdict(list)
        component_values = defaultdict(list)

        for val, org_idx in sorted_pairs:
            root = uf.find(org_idx)
            component_indices[root].append(org_idx)
            component_values[root].append(val)
        
        res = [0] * n
        for root in component_indices:
            sorted_idx_list = sorted(component_indices[root])
            sorted_val_list = component_values[root]

            for idx, val in zip(sorted_idx_list, sorted_val_list):
                res[idx] = val
        return res
        
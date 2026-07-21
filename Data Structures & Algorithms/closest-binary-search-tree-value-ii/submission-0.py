class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        pq = []
        visited = set()

        def dfs(node, pqueue):
            if not node:
                return
            
            if node in visited:
                return

            diff = abs(node.val - target)
            heapq.heappush(pqueue, (diff, node.val))
            visited.add(node)

            dfs(node.left, pqueue)
            dfs(node.right, pqueue)
        
        dfs(root, pq)

        res = []
        while pq and k != 0:
            _, val = heapq.heappop(pq)
            res.append(val)
            k -= 1
        
        return res
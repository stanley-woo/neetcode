"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        def dfs(node, nodeArr):
            if not node:
                return
            
            dfs(node.left, nodeArr)
            nodeArr.append(node)
            dfs(node.right, nodeArr)
        
        arr = []
        dfs(root, arr)

        n = len(arr)
        for i in range(n):
            arr[i].left = arr[i - 1]
            arr[i].right = arr[(i + 1) % n]
        
        return arr[0]
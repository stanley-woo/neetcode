"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        check_sum = 0
        for node in tree:
            check_sum += node.val
            for child in node.children:
                check_sum -= child.val
        
        res = None
        for node in tree:
            if node.val == check_sum:
                res = node
                break
        
        return res
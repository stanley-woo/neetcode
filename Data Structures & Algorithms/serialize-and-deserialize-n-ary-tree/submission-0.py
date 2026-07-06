"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""
class WrappableInt:
    def __init__(self, x):
        self.value = x
    
    def getValue(self):
        return self.value
    
    def increment(self):
        self.value += 1



class Codec:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        """

        serializedList = []
        self._serializedHelper(root, serializedList)

        return "".join(serializedList)

    def _serializedHelper(self, root, listy):
        if not root:
            return
        
        listy.append(chr(root.val + 48))

        listy.append(chr(len(root.children) + 48))

        for child in root.children:
            self._serializedHelper(child, listy)
        

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        """

        if not data:
            return None

        return self._deserializedHelper(data, WrappableInt(0))
    
    def _deserializedHelper(self, data, index):
        if index.getValue() == len(data):
            return None
        
        node = Node(ord(data[index.getValue()]) - 48, [])
        index.increment()
        numChildren = ord(data[index.getValue()]) - 48
        for _ in range(numChildren):
            index.increment()
            node.children.append(self._deserializedHelper(data, index))
        
        return node
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

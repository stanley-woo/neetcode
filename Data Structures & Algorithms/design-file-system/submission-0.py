class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = -1
        
class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        components = path.split("/")

        curr = self.root

        for i in range(1, len(components)):
            name = components[i]

            if name not in curr.children:
                if i == len(components) - 1:
                    curr.children[name] = TrieNode()
                else:
                    return False
            else:
                if i == len(components) - 1:
                    return False

            curr = curr.children[name]
        
        curr.value = value
        return True

    def get(self, path: str) -> int:
        curr = self.root

        components = path.split("/")

        for i in range(1, len(components)):
            name = components[i]

            if name not in curr.children:
                return -1
            curr = curr.children[name]
        return curr.value
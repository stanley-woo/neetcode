class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        self.numMap[val] = 1
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        del self.numMap[val]
        self.size -= 1
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, self.size - 1)
        return list(self.numMap.keys())[idx]
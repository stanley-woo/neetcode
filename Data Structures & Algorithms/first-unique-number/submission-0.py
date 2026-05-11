class FirstUnique:

    def __init__(self, nums: List[int]):
        self.hashMap = defaultdict(int)
        self.stream = deque()
        # self.uniPtr = -1

        for num in nums:
            if self.hashMap[num] == 0:
                self.stream.append(num)
            self.hashMap[num] += 1

    def showFirstUnique(self) -> int:
        while self.stream and self.hashMap[self.stream[0]] > 1:
            self.stream.popleft()

        if self.stream:
            return self.stream[0]
        
        return -1

    def add(self, value: int) -> None:
        if self.hashMap[value] == 0:
            self.stream.append(value)
        
        self.hashMap[value] += 1
        
        # if self.stream and self.stream[0] == value and self.hashMap[value] != 1:
        #     self.stream.popleft()
            


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

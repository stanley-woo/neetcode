class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.slots = set(range(maxNumbers))

    def get(self) -> int:
        if not self.slots:
            return -1
        element = self.slots.pop()
        return element

    def check(self, number: int) -> bool:
        return number in self.slots

    def release(self, number: int) -> None:
        self.slots.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)

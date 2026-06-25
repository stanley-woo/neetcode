class BrowserHistory:

    def __init__(self, homepage: str):
        self.back_stack = [homepage]
        self.forward_stack = []

    def visit(self, url: str) -> None:
        self.back_stack.append(url)
        self.forward_stack = []

    def back(self, steps: int) -> str:
        steps = min(steps, len(self.back_stack)-1)

        while steps:
            res = self.back_stack.pop()
            self.forward_stack.append(res)
            steps -= 1
        return self.back_stack[-1]

    def forward(self, steps: int) -> str:
        steps = min(steps, len(self.forward_stack))
        while steps:
            res = self.forward_stack.pop()
            self.back_stack.append(res)
            steps -= 1
        return self.back_stack[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
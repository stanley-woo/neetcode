class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack_log = []
        res = 0

        for op in operations:
            if op == '+':
                new_score = stack_log[-2] + stack_log[-1]
                stack_log.append(int(new_score))
            elif op == 'D':
                new_score = stack_log[-1] * 2
                stack_log.append(int(new_score))
            elif op == 'C':
                stack_log.pop()
            else:
                stack_log.append(int(op))
        
        res = sum(stack_log)
        return res
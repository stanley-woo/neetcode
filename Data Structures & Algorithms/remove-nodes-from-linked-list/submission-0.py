# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        stack = []

        curr = head
        while curr:
            while stack and curr.val > stack[-1].val:
                stack.pop()
            stack.append(curr)
            curr = curr.next
        
        for i in range(len(stack)-1):
            if i == len(stack) - 2:
                stack[i].next = None
            stack[i].next = stack[i+1]

        return stack[0]   
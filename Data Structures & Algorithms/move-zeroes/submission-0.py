class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue = deque()

        for num in nums:
            if num != 0:
                queue.append(num)
        
        pos = 0
        while queue:
            element = queue.popleft()
            nums[pos] = element
            pos += 1
        
        for i in range(pos, len(nums)):
            nums[i] = 0
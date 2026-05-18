class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, -num)

        n = len(nums)
        for i in range(1, n, 2):
            nums[i] = -heapq.heappop(maxHeap)
        for i in range(0, n, 2):
            nums[i] = -heapq.heappop(maxHeap)
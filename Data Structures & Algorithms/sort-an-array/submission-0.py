class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for num in nums:
            heap.append(num)
        
        heapq.heapify(heap)
        
        for i in range(len(nums)):
            num = heapq.heappop(heap)
            nums[i] = num
        
        return nums
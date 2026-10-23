class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        plans = blocks[:]
        heapq.heapify(plans)
        while len(plans) > 1:
            heapq.heappop(plans)
            longer = heapq.heappop(plans)
            heapq.heappush(plans, longer + split)
        return plans[0]

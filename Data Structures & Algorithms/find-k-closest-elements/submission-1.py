class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []
        ans = []

        for num in arr:
            pq.append((abs(num - x), num))
        heapq.heapify(pq)
        while k:
            _, num = heapq.heappop(pq)
            ans.append(num)
            k -= 1
        ans.sort()
        return ans
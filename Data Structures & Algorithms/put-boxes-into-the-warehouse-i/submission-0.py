class Solution:
    def maxBoxesInWarehouse(self, boxes: list[int], warehouse: list[int]) -> int:
        boxes.sort()

        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i], warehouse[i-1])
        
        res = 0
        box_idx = 0
        for i in range(len(warehouse)-1, -1, -1):
            if box_idx == len(boxes):
                break
            if boxes[box_idx] <= warehouse[i]:
                res += 1
                box_idx += 1
        return res
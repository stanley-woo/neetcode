class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(k):
            ship_days = 1
            cur_weight = 0
            for weight in weights:
                if cur_weight + weight > k:
                    ship_days += 1
                    cur_weight = 0
            
                cur_weight += weight
            return ship_days <= days
        
        lo, hi = max(weights), sum(weights)
        res = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if can_ship(mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return res
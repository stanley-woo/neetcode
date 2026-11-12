class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        n, m = len(spells), len(potions)

        potions.sort()

        def binary_search(strength):
            low, high = 0, m - 1
            res_idx = -1
            while low <= high:
                mid = low + (high - low) // 2
                if potions[mid] * strength >= success:
                    res_idx = mid
                    high = mid - 1
                else:
                    low = mid + 1

            if res_idx == -1:
                return 0
            return m - res_idx

        res = []
        for spell in spells:
            pairs = binary_search(spell)
            res.append(pairs)

        return res

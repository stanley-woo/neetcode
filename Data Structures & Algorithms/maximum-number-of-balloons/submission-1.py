class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_table = {}
        for char in text:
            if char in "balon":
                hash_table[char] = hash_table.get(char, 0) + 1
        
        if len(hash_table) < 5:
            return 0
        
        hash_table['l'] //= 2
        hash_table['o'] //= 2
        return min(hash_table.values())
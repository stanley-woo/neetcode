class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_map = {}

        for char in allowed:
            allowed_map[char] = allowed_map.get(char, 0) + 1
        
        res = 0
        for word in words:
            consistent = True
            for char in word:
                if char not in allowed_map.keys():
                    consistent = False
                    break
            
            if consistent:
                res += 1
        return res
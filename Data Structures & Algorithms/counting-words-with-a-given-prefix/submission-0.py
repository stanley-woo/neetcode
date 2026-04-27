class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0

        for i in range(len(words)):
            if len(pref) > len(words[i]):
                continue
            
            isPre = True
            for j in range(len(pref)):
                if pref[j] != words[i][j]:
                    isPre = False
                    break
            
            if isPre:
                res += 1
        
        return res
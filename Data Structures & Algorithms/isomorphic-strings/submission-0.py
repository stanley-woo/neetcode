class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_s, hash_t = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if ((c1 in hash_s and hash_s[c1] != c2)) or ((c2 in hash_t and hash_t[c2] != c1)):
                return False
            hash_s[c1] = c2
            hash_t[c2] = c1
        return True
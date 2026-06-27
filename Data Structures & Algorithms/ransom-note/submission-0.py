class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counterRansom = Counter(ransomNote)
        counterMagazine = Counter(magazine)

        for char in ransomNote:
            if char not in counterMagazine:
                return False

            if counterRansom[char] > counterMagazine[char]:
                return False
        return True
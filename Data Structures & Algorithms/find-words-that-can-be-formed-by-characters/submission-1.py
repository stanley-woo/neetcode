class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        counter = {}
        for char in chars:
            counter[char] = counter.get(char, 0) + 1

        for word in words:
            word_counter = {}
            for char in word:
                word_counter[char] = word_counter.get(char, 0) + 1
            match = True
            for char, count in word_counter.items():
                if char not in counter or counter[char] < count:
                    match = False
                    break
            if match:
                res += len(word)

        return res
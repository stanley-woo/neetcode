class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_hash(string: str):
            key = []
            for i in range(1, len(string)):
                # Calculate circular distance between adjacent characters
                diff = (ord(string[i]) - ord(string[i-1])) % 26
                key.append(str(diff))
            return '.'.join(key)
        
        groups = defaultdict(list)
        for string in strings:
            hash_key = get_hash(string)
            groups[hash_key].append(string)
        
        return list(groups.values())
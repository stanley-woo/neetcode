class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        distinct_arr = []
        for char in arr:
            if counter[char] == 1:
                distinct_arr.append(char)
        
        if len(distinct_arr) < k:
            return ""
        
        return distinct_arr[k-1]
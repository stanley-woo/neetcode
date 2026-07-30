class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        res = [[], []]

        for num in counter1.keys():
            if num not in counter2:
                res[0].append(num)
        
        for num in counter2.keys():
            if num not in counter1:
                res[1].append(num)
        
        return res
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set, nums2_set = set(nums1), set(nums2)
        res = set()
        l1, l2 = len(nums1), len(nums2)

        if l1 >= l2:
            for i in range(len(nums1)):
                if nums1[i] in nums2_set and nums1[i] not in res:
                    res.add(nums1[i])
        else:
            for i in range(len(nums2)):
                if nums2[i] in nums1_set and nums2[i] not in res:
                    res.add(nums2[i])
        
        return list(res)
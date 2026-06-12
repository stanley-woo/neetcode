class SparseVector:
    def __init__(self, nums: List[int]):
        self.hashtable = set()
        self.nums = nums
        for i in range(len(nums)):
            if nums[i] != 0:
                self.hashtable.add(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in range(len(vec.nums)):
            if vec.nums[i] != 0 and i in self.hashtable:
                res += vec.nums[i] * self.nums[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

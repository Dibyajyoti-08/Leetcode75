class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        numsSet1, numsSet2 = set(nums1), set(nums2)
        res1, res2 = set(), set()
        [res1.add(i) for i in nums1 if i not in numsSet2]
        [res2.add(i) for i in nums2 if i not in numsSet1]
        return [list(res1), list(res2)]
        
# ----------------------------------------------------------------

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set (nums2)
        
        return [list(s1 - s2), list(s2 - s1)]
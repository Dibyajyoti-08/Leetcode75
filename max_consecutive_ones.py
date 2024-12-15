class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, mxm, nz = 0, 0, 0
        for r in range(len(nums)):
            nz += 1 if nums[r] == 0 else 0
            while nz > k:
                nz -= 1 if nums[l] == 0 else 0
                l += 1
            w = r - l + 1
            mxm = max(mxm, w)
        return mxm

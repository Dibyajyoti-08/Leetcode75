class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, nr, mxm = 0, 0, 0
        for r in range(len(nums)):
            nr += 1 if nums[r] == 0 else 0
            while nr > 1:
                nr -= 1 if nums[l] == 0 else 0
                l += 1
            w = r - l + 1
            mxm = max(w, mxm)
        return mxm - 1

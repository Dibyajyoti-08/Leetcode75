class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for i in range(k):
            curr += nums[i]
        mxm = curr
        for i in range(k, len(nums)):
            curr += nums[i]
            curr -= nums[i-k]
            mxm = max(curr, mxm)
        return mxm / k

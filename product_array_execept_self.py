class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = [1] * len(nums)
        left = 1
        right = 1
        for i in range(len(nums)):
            op[i] *= left
            left *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            op[i] *= right
            right *= nums[i]
        return op

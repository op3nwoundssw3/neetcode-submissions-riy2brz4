class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rez = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            rez[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            rez[i] *= postfix
            postfix *=nums[i]
        return rez
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]
        while r > l:
            m = l + (r-l) // 2
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                r = m
        return nums[l]
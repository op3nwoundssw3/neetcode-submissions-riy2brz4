class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:#deepseek
        return len(nums) != len(set(nums))
        
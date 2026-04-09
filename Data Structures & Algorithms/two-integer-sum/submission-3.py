class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict() #values : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in d:
                return [d[diff], i]
            else:
                d[n] = i
            
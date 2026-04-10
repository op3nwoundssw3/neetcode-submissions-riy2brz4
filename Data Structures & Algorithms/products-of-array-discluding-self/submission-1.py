class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rez = []
        for i in range(len(nums)):
            if nums[i] !=0:
                number = nums[i]
            else:
                number = 1
            for j in range(len(nums)):
                if i != j:
                    number *= nums[j]
            if nums[i] != 0:
                rez.append(int(number/nums[i]))
            else:
                rez.append(int(number/1))
        return rez
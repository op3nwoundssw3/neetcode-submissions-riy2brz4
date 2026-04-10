class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        newnums = sorted(set(nums))
        counter = 1
        maximus = 1
        for i in range(len(newnums)-1):
            if newnums[i+1] - newnums[i] == 1:
                counter +=1 
                maximus = max(maximus,counter)
            else:
                counter = 1
        return maximus
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxim = 0
        while l < r:
            area = (r-l) * min(heights[r],heights[l])
            maxim = max(maxim, area)
            if heights[r] <= heights[l]:
                r -= 1
            else:
                l += 1
        return maxim 
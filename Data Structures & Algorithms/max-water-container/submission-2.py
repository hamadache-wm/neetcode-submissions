class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        max_height = max(heights)
        i = 0
        j = len(heights) - 1
        while i < j:
            output = max(min(heights[i], heights[j]) * (j - i), output)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            if output > max_height * (j - i):
                break
        return output
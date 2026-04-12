class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        
        for i, e in enumerate(heights):
            for j, e2 in enumerate(heights[i+1:], start=i+1):
                area = min(e, e2) * (j - i)
                output = area if area > output else output

        return output
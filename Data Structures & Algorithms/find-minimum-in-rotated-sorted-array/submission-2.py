class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        m = len(nums)
        r = m - 1
        res = nums[0]
        
        while nums[l] > nums[r]:
            m = m // 2 if m != 1 else 1
            res = min(res, nums[l], nums[r])

            if nums[l + m] > nums[l]:
                l = l + m
            else:
                r = r - m
            
            res = min(res, nums[l], nums[r])

        return res
        
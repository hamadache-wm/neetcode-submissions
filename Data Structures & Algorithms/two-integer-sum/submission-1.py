class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, element_i in enumerate(nums):
            for j, element_j in enumerate(nums[i+1:], start=i+1):
                sum = element_i + element_j
                if sum == target:
                    return [i, j]
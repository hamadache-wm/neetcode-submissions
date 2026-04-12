class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsInArray = []
        for x in nums:
            if numsInArray.count(x) == 0:
                numsInArray.append(x)
            else:
                return True
        
        return False
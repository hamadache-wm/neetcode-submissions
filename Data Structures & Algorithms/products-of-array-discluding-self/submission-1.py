class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        res = []

        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                product = product * n
        
        match zero_count:
            case 0:
                for i in range(len(nums)):
                    res.append(int(product/nums[i]))
            case 1:
                for n in nums:
                    if n == 0:
                        res.append(int(product))
                    else:
                        res.append(0)
            case _:
                res = [0]*len(nums)

        return res
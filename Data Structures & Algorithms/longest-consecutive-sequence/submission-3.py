class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        sorted_nums_set = sorted(nums_set)
        tuple_sorted_nums = tuple(sorted_nums_set)

        print(tuple_sorted_nums)

        prev = tuple_sorted_nums[0]
        res = 1
        all_res = []

        for i in range(1, len(tuple_sorted_nums)):
            exp = prev + 1
            curr = tuple_sorted_nums[i]

            if curr != exp:
                all_res.append(res)
                res = 0
            
            res += 1
            prev = curr

        all_res.append(res)

        return max(all_res)
        
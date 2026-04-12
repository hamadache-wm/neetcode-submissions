class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_set = set(nums)
        nums_dict = dict.fromkeys(nums_set, 0)
        res = []
        
        for e in nums_set:
            nums_dict[e] = nums.count(e)

        for i in range(k):
            max_key = max(nums_dict, key=nums_dict.get)
            res.append(max_key)
            del nums_dict[max_key]

        return res
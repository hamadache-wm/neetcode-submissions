class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        alr_added = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        alr_added_flag = False

                        for e in alr_added:
                            if e == tuple(sorted([nums[i], nums[j], nums[k]])):
                                print("2@@@22")
                                alr_added_flag = True
                        
                        if alr_added_flag == False:
                            alr_added.append(tuple(sorted([nums[i], nums[j], nums[k]])))
                            res.append([nums[i], nums[j], nums[k]])
                        
        return res

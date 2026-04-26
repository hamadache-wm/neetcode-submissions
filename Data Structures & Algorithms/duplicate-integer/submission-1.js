class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const dupSet = new Set(nums);

        return dupSet.size !== nums.length
    }
}

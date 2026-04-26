class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const dupSet = new Set([]);

        for (const n of nums) {
            if (dupSet.has(n)) {
                return true;
            }
            dupSet.add(n);
        }

        return false;
    }
}

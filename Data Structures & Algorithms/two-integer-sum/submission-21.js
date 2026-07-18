class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const indices = new Map()
        for (let i =0; i< nums.length; i++){
            let diff = target - nums[i]

            if (indices.has(diff)){
                return [indices.get(diff), i]
            }
            indices.set(nums[i], i)
        }

        return []
    }
}

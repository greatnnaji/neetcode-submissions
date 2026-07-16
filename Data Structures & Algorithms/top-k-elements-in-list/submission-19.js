class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let count = {}
        nums.forEach(val => (count[val] = (count[val] || 0) + 1))

        let freq = [[]]
        for(const num in nums){
            freq.push([])
        }

        for (const [val, occ] of Object.entries(count)){
            freq[occ].push(val)
        }

        let i = freq.length - 1
        let res = []
        while (i > 0){
            for (const item of freq[i]){
                res.push(item)
                if (res.length == k){
                    return res
                }
            }
            i --
        }
        return []
    }
}

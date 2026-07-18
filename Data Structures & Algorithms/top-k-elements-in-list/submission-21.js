class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let count = new Map()
        nums.forEach(val => {
            count.set(val, (count.get(val) || 0) + 1)
        })
        let freq = Array.from({length: nums.length + 1}, () => [])
        count.forEach((occ, val) => {
            freq[occ].push(val)
        })
        let res = []
        for (let i = freq.length - 1; i > 0; i --){
            for (const num of freq[i]){
                res.push(num)
                if (res.length === k){
                    return res
                }
            }
        }

    }
}

class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let count = new Map()
        nums.forEach(val => (count.set(val, (count.get(val) || 0) + 1)))

        let freq = Array.from({length: nums.length + 1}, () => []);

        for (const [val, occ] of count){
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

class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false
        let freq_s = new Map()
        for (const c of s){
            freq_s.set(c, (freq_s.get(c) || 0) + 1)
        }
        for (const c of t){
            let count = freq_s.get(c) || 0
            if (count === 0) return false
            freq_s.set(c, count - 1)
        }

        return true
    }
}

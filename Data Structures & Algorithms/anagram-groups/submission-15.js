class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let group_anagram = new Map()
        for (let i = 0; i < strs.length; i++){
            let count = new Array(26).fill(0)

            for (const c of strs[i]){
                count[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
            }
            let key = count.join(',')
            if (!group_anagram.has(key)){
                group_anagram.set(key, [])
            }
            group_anagram.get(key).push(strs[i])
        }

        return Array.from(group_anagram.values())
    }
}

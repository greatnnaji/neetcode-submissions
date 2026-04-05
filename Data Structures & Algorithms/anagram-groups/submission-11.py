class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_hashmap = {}

        for string in strs:
            joined_sorted_string = "".join(sorted(string))
            if joined_sorted_string in string_hashmap: #checks keys
                string_hashmap[joined_sorted_string].append(string)
            else:
                string_hashmap[joined_sorted_string] = [string]
        
        # print(string_hashmap)

        group_anagrams = []

        for sorted_str, string_arr in string_hashmap.items():
            group_anagrams.append(string_arr)
        
        print(group_anagrams)
        
        return group_anagrams
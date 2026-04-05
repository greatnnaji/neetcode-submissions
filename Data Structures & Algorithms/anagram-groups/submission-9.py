class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_arr = []
        strs_hashmap = dict()
        for index,string in enumerate(strs):
            sorted_str = "".join(sorted(string))
            if sorted_str in strs_hashmap:
                strs_hashmap[sorted_str].append(string)
            else:
                strs_hashmap[sorted_str] = [string] # biggest issue: adding square brackets -> this initializes and array, otherwise append doesn't work
        
        for value_array in strs_hashmap.values():
            output_arr.append(value_array)

        print(output_arr)

        return output_arr

    # answer at the end why using Counter from collections doesn't work
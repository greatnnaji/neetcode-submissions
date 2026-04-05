class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = dict()
        for string in strs:
            sorted_chars = sorted(string)
            key = ''.join(sorted_chars)

            if key in anagrams_dict:
                anagrams_dict[key].append(string)
            else:
                anagrams_dict[key] = [string]
            
        result = []
        for value in anagrams_dict.values():
            result.append(value)
        
        return result

        # Note: Sets are not hashable - You can't put a regular set inside another set 
        # because sets are mutable and therefore not hashable.


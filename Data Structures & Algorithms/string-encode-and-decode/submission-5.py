class Solution:

    def encode(self, strs: List[str]) -> str:
        result_str = ""

        for string in strs:
            result_str += str(len(string)) + "#" + string

        return result_str

    def decode(self, s: str) -> List[str]:
        result_list = []
        i = 0
        while i < len(s):
            j = i
            new_str = ""
            while s[j] != "#":
                j += 1
        
            length = int(s[i:j])
            new_str = s[j+1:j+1+length]
            result_list.append(new_str)
            i = j + 1 + length

        return result_list
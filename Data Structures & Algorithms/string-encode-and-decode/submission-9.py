class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        
        return encoded_str


    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            num_len = ""
            while s[i] != "#":
                num_len += s[i]
                i += 1
            int_len = int(num_len)
            
            i += 1

            new_str = ""
            j = i

            while i < int_len + j:
                new_str += s[i]
                i += 1

            strs.append(new_str)

        return strs
            




                



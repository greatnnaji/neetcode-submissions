class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string

        print(encoded)

        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []

        index = 0
        while index < len(s):
            string_len = ""
            while s[index] != '#':
                # print("adding: ", s[index])
                string_len += s[index]
                index += 1
            
            string_len = int(string_len)

            index += 1

            newString = ""
            cur_index = index
            while index < string_len + cur_index :
                newString += s[index]
                index += 1
            
            print(newString)

            decoded.append(newString)

        # print(decoded)
        return decoded


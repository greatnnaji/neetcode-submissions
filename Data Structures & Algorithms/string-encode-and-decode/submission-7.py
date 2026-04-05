class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for string in strs:
            encoded += str(len(string)) + '#' + string
        
        print(encoded)

        return encoded

    def decode(self, s: str) -> List[str]:
        index = 0
        string_length = ''

        decoded = []

        while index < len(s):
            print(s[index])
            while s[index] != '#':
                string_length += s[index]
                index += 1
            
            # currently at index with char = #
            
            index += 1

            new_string = ''

            # print(string_length)

            total = index + int(string_length)

            while index < total:
                new_string += s[index]
                index += 1
            
            # print(new_string)
            decoded.append(new_string)
            # print(decoded)
            new_string = ''
            string_length = ''

        return decoded

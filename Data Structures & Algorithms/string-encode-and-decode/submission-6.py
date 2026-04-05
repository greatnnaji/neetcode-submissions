class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''

        for string in strs:
            encoded_string += str(len(string)) + "#" + string

        print(encoded_string)

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_str = []

        index = 0 # use as pointer

        while index < len(s):
            current_string = ""
            string_length = ""

            while s[index] != "#":
                string_length += s[index]
                index += 1
            
            index += 1
            print(string_length)
            print(index)

            string_length = int(string_length)
            total_length = index + string_length
            print(total_length)

            while index < total_length:
                current_string += s[index]
                index += 1
            
            print(current_string)

            decoded_str.append(current_string)

            print(decoded_str)

        return decoded_str

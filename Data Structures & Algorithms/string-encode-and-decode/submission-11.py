class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for s in strs:
            encoded += str(len(s)) + '#' + s

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1
            
            length = int(length)

            i += 1
            
            new = ''
            j = i + length
            while i < j:
                new += s[i]
                i += 1
            
            decoded.append(new)
        
        return decoded




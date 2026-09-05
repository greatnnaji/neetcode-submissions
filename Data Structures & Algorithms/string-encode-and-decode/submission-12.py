class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):

            j = s.find("#", i)

            length = int(s[i:j])

            i = j + 1

            new = s[i: i + length]

            i = i + length

            decoded.append(new)
        
        return decoded




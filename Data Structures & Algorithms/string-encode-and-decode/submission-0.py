class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for i in strs:
            res.append(f"{len(i)}#{i}")
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])

            # Extract the actual word right after '#'
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            # Jump i to the start of the next length header
            i = j + 1 + length
        return res



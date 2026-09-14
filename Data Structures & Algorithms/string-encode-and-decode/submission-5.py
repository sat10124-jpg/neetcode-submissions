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
            
            length_of_word = int(s[i:j])

            word = s[j+1:j+1+length_of_word]
            res.append(word)
            i = j + 1 + length_of_word
        return res

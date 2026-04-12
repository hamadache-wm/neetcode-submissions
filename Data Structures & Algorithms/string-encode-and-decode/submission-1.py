class Solution:
    CHAR_SEPARATOR = "-"
    WORD_SEPARATOR = ","

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            for i, c in enumerate(s):
                res += str(ord(s[i])) + self.CHAR_SEPARATOR
            res += self.WORD_SEPARATOR
    
        return res
                

    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        letter = ""

        for c in s:
            if c == self.WORD_SEPARATOR:
                res.append(word)
                word = ""
            elif c == self.CHAR_SEPARATOR:
                word += chr(int(letter))
                letter = ""
            else:
                letter += c
    
        return res

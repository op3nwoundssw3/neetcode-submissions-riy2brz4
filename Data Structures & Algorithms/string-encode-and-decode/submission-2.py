class Solution:

    def encode(self, strs: List[str]) -> str:
        rez = ""
        for s in strs:
            rez += str(len(s)) + '#' + s
        return rez
    def decode(self, s: str) -> List[str]:
        rez, i = [], 0
        while i<len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+length+1]
            i = j + 1 + length
            rez.append(word)
        return rez
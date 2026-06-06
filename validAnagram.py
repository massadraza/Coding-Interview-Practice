class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        lettersJ = {}

        if(len(s) != len(t)):
            return False

        for i in range(len(s)):
            letters[s[i]] = letters.get(s[i], 0) + 1

        for j in range(len(t)):
            lettersJ[t[j]] = lettersJ.get(t[j], 0) + 1


        if letters == lettersJ:
            return True

        return False
            
        
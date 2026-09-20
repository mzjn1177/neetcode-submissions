class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(0, len(s)):
                frequency[s[i]] =  s.count(s[i])

            for x, y in frequency.items():
                if y != t.count(x):
                    return False
        return True


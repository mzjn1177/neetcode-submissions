class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n = {}
        m = {}

        if sorted(n.keys()) != sorted(m.keys()):
            return False
        else:
            for c in s:
                if c in n.keys():
                    pass
                else:
                    n[c] = s.count(c)

            for x in t:
                if x in m.keys():
                    pass
                else:
                    m[x] = t.count(x)
        return n == m

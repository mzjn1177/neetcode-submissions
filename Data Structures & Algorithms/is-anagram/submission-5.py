class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n = {}
        m = {}

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
        print(n)
        print(m)

        if sorted(n.keys()) != sorted(m.keys()):
            return False
        else:
            for k in n.keys():
                if n[k] != m[k]:
                    print(n[k])
                    print(m[k])
                    return False
        return True
        
        
      
      
      
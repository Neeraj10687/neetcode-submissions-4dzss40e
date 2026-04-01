class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sset={}
        tset={}
        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            sset[s[i]] = 1+sset.get(s[i],0)
        for i in range(len(t)):
            tset[t[i]] = 1+tset.get(t[i],0)

        return sset==tset
        
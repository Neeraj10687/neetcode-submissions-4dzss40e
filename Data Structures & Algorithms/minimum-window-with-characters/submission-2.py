class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t =="": return ""
        twin,win={},{}

        for c in t:
            twin[c]=1+twin.get(c,0)

        have,need=0,len(twin)
        l=0
        res,reslen=[-1,-1],float("infinity")

        for r in range(len(s)):
            p=s[r]

            win[p]=1+win.get(p,0)

            if p in twin and twin[p]==win[p]:
                have +=1
            
            while have == need:
                if (r-l+1)<reslen:
                    reslen=(r-l+1)
                    res=[l,r]
                
                win[s[l]] -=1
                if s[l] in twin and win[s[l]] <twin[s[l]]:
                    have -=1
                l +=1
        l,r=res
        return s[l:r+1] if reslen != float("infinity") else ""

        
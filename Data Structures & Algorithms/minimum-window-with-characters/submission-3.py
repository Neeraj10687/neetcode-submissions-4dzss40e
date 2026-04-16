class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t =="": return ""
        twi,win={},{}

        for c in t:
            twi[c]=1+twi.get(c,0)

        have,need=0,len(twi)
        l=0
        res,reslen=[-1,-1],float("infinity")

        for r in range(len(s)):
            p=s[r]

            win[p]=1+win.get(p,0)

            if p in twi and twi[p]==win[p]:
                have +=1
            
            while have == need:
                if (r-l+1)<reslen:
                    reslen=(r-l+1)
                    res=[l,r]
                
                win[s[l]] -=1
                if s[l] in twi and win[s[l]] <twi[s[l]]:
                    have -=1
                l +=1
        l,r=res
        return s[l:r+1] if reslen != float("infinity") else ""

        
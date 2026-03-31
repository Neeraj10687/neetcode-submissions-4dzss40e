class Solution:
    def minWindow(self, s: str, t: str) -> str:


        counT={}
        win={}
        have=0
        res=[-1,-1]


        if t=="": return ""

        for c in t:
            counT[c]=1+counT.get(c,0)
        
        resLen=float("infinity")
        need=len(counT)
        l=0
        for r in range(len(s)):
            c=s[r]
            win[c]=1+win.get(c,0)

            if c in counT and win[c] ==counT[c]:
                have +=1

            while have ==need:
                if(r-l+1)<resLen:
                    res=[l,r]
                    resLen=(r-l+1)
                
                win[s[l]] -=1
                if s[l] in counT and win[s[l]]<counT[s[l]]:
                    have -=1
                l+=1

        l,r =res
        return  s[l:r+1] if resLen !=float("infinity") else ""
            


 
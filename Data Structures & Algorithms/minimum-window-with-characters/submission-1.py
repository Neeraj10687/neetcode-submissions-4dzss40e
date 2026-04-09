class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="": return ""

        Twin,win={},{}
         
        for i in t:
            Twin[i]=1+Twin.get(i,0)
        
        have,need=0,len(Twin)
        res,resLen=[-1,-1],float("infinity")
        l=0

        for r in range(len(s)):
            i=s[r]
            win[i]=1+win.get(i,0)

            if i in Twin and win[i]==Twin[i]:
                have +=1
            
            while have == need:
                if r-l+1 < resLen:
                    resLen =(r-l+1)
                    res=[l,r]

                win[s[l]] -=1
                if s[l] in Twin and Twin[s[l]]> win[s[l]]:
                    have -=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen != float("infinity") else ""




        
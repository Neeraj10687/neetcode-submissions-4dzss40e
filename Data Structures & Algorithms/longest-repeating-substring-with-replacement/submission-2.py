class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        coun={}
        res=0

        l=0
        for r in range(len(s)):
            coun[s[r]] = 1+coun.get(s[r],0)
            while (r-l+1) - max(coun.values())>k:
                coun[s[l]] -=1
                l+=1
            res=max(res,r-l+1)
        return res
                
        
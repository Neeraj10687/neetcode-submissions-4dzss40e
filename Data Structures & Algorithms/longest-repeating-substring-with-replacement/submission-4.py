class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c={}
        res=0
        l=0

        for i in range(len(s)):
            c[s[i]]=1+c.get(s[i],0)
            mf=max(c.values())

            if i-l+1 - mf>k:
                c[s[l]] -=1
                l+=1
            res=max(res,i-l+1)
        return res

        
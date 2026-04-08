class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cn={}
        res=0
        l=0

        for i in range(len(s)):
            cn[s[i]]=1+cn.get(s[i],0)
            mf=max(cn.values())

            if i-l+1 - mf>k:
                cn[s[l]] -=1
                l+=1
            res=max(res,i-l+1)
        return res

        
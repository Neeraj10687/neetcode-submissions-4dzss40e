class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=set()
        l=0
        mp=0

        for i in range(len(s)):
            while s[i]  in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[i])

            mp=max(mp,i-l+1)
        return mp
        
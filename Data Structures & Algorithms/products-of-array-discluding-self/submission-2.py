class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref=[0]*len(nums)
        pref[0]=1

        suf=[0]*len(nums)
        suf[len(nums)-1]=1
        res=[0]*len(nums)
        
        for i in range(1,len(nums)):
            
            pref[i] =nums[i-1] * pref[i-1]
        
        suf[len(nums)-1]=1

        for i in range(len(nums)-2,-1,-1):
            suf[i] = nums[i+1] * suf[i+1]

        for i in range(len(nums)):
            res[i] = pref[i]* suf[i]
        return res
    
        


        
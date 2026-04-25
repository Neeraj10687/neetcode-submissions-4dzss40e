class Solution:
    def findMin(self, nums: List[int]) -> int:
        re=nums[0]
        l,r=0,len(nums)-1

        while l<=r:
            if nums[l]<nums[r]:
                re=min(re,nums[l])
                break
            
            m=(l+r)//2
            re=min(re,nums[m])
            if nums[m] >= nums[l]:
                l=m+1
            else:
                r=m-1
        return re
        
        
         
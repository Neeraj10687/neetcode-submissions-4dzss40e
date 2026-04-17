class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()

        i=1

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1] :
                continue

            a=nums[i]
            l,r=i+1,len(nums)-1

            while l<r:
                tsum =a+nums[l]+nums[r]

                if tsum < 0:
                    l+=1
                elif tsum >0:
                    r -=1
                else:
                    ans.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1

                    while l<r and nums[l] ==nums[l-1]:
                        l+=1
                        
        return ans

        
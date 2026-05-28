class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ogarr=[]

        for i,a in enumerate(nums):
            ogarr.append([a,i])


        ogarr.sort()


        l=0
        r=len(nums)-1

        while l<r:
            sum =ogarr[l][0]+ogarr[r][0]
            if sum ==target:
                return [min(ogarr[l][1],ogarr[r][1]),
                        max(ogarr[l][1],ogarr[r][1])]
            elif sum <target:
                l+=1
            else:
                r-=1
        return []


        
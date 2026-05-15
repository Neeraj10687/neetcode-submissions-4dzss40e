class Solution:
    def threeSum(self, num: List[int]) -> List[List[int]]:
        ans=[]
        num.sort()

        i=1

        for i in range(len(num)):
            if i>0 and num[i] == num[i-1] :
                continue

            a=num[i]
            l,r=i+1,len(num)-1

            while l<r:
                tsum =a+num[l]+num[r]

                if tsum < 0:
                    l+=1
                elif tsum >0:
                    r -=1
                else:
                    ans.append([a,num[l],num[r]])
                    l+=1
                    r-=1

                    while l<r and num[l] ==num[l-1]:
                        l+=1
                        
        return ans
        

        
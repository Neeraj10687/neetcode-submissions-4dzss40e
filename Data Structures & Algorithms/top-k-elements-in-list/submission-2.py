class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums.sort()
        seet={}

        for i in range(len(nums)):
            seet[nums[i]]=1+seet.get(nums[i],0)
        
        arr=[] 
        for i,a in seet.items():
            arr.append([a,i])
        arr.sort()

        res=[]

        while len(res)<k:
            res.append(arr.pop()[1])
        return res

        
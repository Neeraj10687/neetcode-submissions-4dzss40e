class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cn =len(nums)

        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                tmp=nums[k]
                nums[k]=nums[i]
                nums[i]=tmp
                k+=1

        return k
        
        
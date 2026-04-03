class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nms=set(nums)
        length=0

        for n in nums:
            if (n-1) not in nums:
                leng=0

                while (n+leng) in nums:
                    leng+=1

                length=max(leng,length)
        return length
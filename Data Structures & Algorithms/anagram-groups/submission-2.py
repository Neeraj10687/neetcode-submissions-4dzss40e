class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s={}
        
        res=defaultdict(list)

        for i in strs:
            ss=''.join(sorted(i))
            res[ss].append(i)
        return list(res.values())

        
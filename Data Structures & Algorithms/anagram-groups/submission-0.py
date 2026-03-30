class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =defaultdict(list)

        for s in strs:
            Ssorted=''.join(sorted(s))
            res[Ssorted].append(s)
        return list(res.values())
        
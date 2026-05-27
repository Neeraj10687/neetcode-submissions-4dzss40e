class Solution:
    def isValid(self, s: str) -> bool:

        stak =[]
        par={")" : "(","]":"[","}" :"{"}

        for c in s:
            if c in  par:
                if stak and stak[-1]==par[c]:
                    stak.pop()
                else:
                    return False
            else:
                stak.append(c)
        return True if not stak else False

        
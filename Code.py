class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        t = sorted(score,reverse=True)
        print(t)
        s = []
        for x in t:
            s.append(str(t.index(x)+1))
        if "1" in s:
            s[0] = "Gold Medal"
        if "2" in s:
            s[1] = "Silver Medal"
        if "3" in s:
            s[2] = "Bronze Medal"
        d = {}
        for i in range(len(t)):
            d[t[i]] = s[i]
        s2 = []
        for k in score:
            s2.append(d[k])
        return s2

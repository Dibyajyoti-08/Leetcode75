class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = {}
        for i in arr:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
        hmLst = list(hm.values())
        hmSt = set()
        for i in hmLst:
            hmSt.add(i)
        return len(hmLst) == len(hmSt)
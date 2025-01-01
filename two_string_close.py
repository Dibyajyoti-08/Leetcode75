class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # if len(word1) != len(word2):
        #     return False
        # from collections import Counter
        # cnt1 = Counter(word1)
        # cnt2 = Counter(word2)
        # return (cnt1.keys() == cnt2.keys()) and (sorted(cnt1.values()) == sorted(cnt2.values()))
        if len(word1) != len(word2):
            return False
        hm1 = {}
        hm2 = {}
        for i in word1:
            if i in hm1:
                hm1[i] += 1
            else:
                hm1[i] = 1
        for i in word2:
            if i in hm2:
                hm2[i] += 1
            else:
                hm2[i] = 1
        return (hm1.keys() == hm2.keys()) and (sorted(hm1.values()) == sorted(hm2.values()))
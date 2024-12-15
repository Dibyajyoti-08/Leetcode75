class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, count, mxm = 0, 0, 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for r in range(len(s)):
            count += 1 if s[r] in vowels else 0
            if r - l + 1 > k:
                count -= 1 if s[l] in vowels else 0
                l += 1
            mxm = max(mxm, count)
        return mxm

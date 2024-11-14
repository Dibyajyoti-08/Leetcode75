class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        l = min(len(word1), len(word2))
        for i in range(l):
            output += word1[i] + word2[i]
        if len(word1) > l:
            output += word1[l:]
        if len(word2) > l:
            output += word2[l:]
        return output

if __name__  == '__main__':
    word1 = input("Enter your first word: ")
    word2 = input("Enter your second word: ")
    solution = Solution()
    print(solution.mergeAlternately(word1, word2))


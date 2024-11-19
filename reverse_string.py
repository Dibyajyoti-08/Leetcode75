class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = list(s)
        op = []
        for i in range(len(s) -1, -1, -1):
            op.append(s[i])

            if i != 0:
                op.append(" ")
        return "".join(op)
        

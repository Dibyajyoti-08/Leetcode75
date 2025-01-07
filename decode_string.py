class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                str = ""
                while stack and stack[-1] != '[':
                    str = stack.pop() + str
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(str * int(num))
        return "".join(stack)
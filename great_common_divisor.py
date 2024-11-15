class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        from math import gcd
        return str1[:gcd(len(str1), len(str2))]

if __name__ == '__main__':
    solution = Solution()
    str1 = input('Enter first string: ')
    str2 = input('Enter second string: ')
    print('Your GCD of two string inputs: ')
    print(solution.gcdOfStrings(str1, str2))

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0

        while j < len(chars):
            char = chars[j]
            count = 0

            while j < len(chars) and chars[j] == char:
                count += 1
                j += 1
            
            chars[i] = char
            i += 1

            if count > 1:
                for digit in str(count):
                    chars[i] = digit
                    i += 1
        return i

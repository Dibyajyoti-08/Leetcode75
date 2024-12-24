class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        op = [0]
        for i in range(len(gain)):
            op.append(op[-1] + gain[i])

        return max(op)
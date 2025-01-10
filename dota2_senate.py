class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        senate = list(senate)
        R, D = deque(), deque()
        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)
        while R and D:
            r = R.popleft()
            d = D.popleft()

            if r < d:
                R.append(r + len(senate))
            else:
                D.append(d + len(senate))
        return "Radiant" if R else "Dire"
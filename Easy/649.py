from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant_queue = deque()
        dire_queue = deque()

        # Store indices of R and D senators
        for i, senator in enumerate(senate):
            if senator == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        # Simulate the voting process
        while radiant_queue and dire_queue:
            r_index = radiant_queue.popleft()
            d_index = dire_queue.popleft()

            # The senator with the smaller index bans the other
            if r_index < d_index:
                radiant_queue.append(r_index + n)  # Move to next round
            else:
                dire_queue.append(d_index + n)

        return "Radiant" if radiant_queue else "Dire"


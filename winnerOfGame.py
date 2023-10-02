class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0

        for i in range(1, len(colors) - 1):
            current_color = colors[i]
            next_color = colors[i+1]
            prev_color = colors[i-1]

            if current_color == 'A' and next_color == 'A' and prev_color == 'A':
                alice += 1
            elif current_color == 'B' and next_color == 'B' and prev_color == 'B':
                bob += 1
        return alice > bob
"""Contains custom exception classes for a game"""

class GameOver(Exception):
    """Raise this exception when the game is over and save the player's score to a file"""
    def __init__(self, score, name, mode):
        """
        Initialize GameOver exception
        """
        self.score = score
        self.name = name
        self.mode = mode

    def save_score(self):
        """
        Save the player's score to a file

        The score is saved to a file called 'scores.txt'.
        The file contains the top 10 scores, sorted by score in descending order.
        Each line in the file has the following format:
        <name> <score> (<mode>)
        """
        with open('scores.txt', 'a', encoding='utf-8') as file_scores:
            file_scores.write(f"{self.name}: {self.score} ({self.mode})\n")

        scores = []
        with open('scores.txt', 'r', encoding='utf-8') as file_scores:
            for line in file_scores:
                line = line.strip()
                if line:
                    name, score, mode = line.split()
                    score = int(score.strip())
                    mode = mode.strip()[1:-1]
                    scores.append((name, score, mode))

        scores.sort(key=lambda x: x[1], reverse=True)

        scores = scores[:10]

        with open('scores.txt', 'w', encoding='utf-8') as file_scores:
            for name, score, mode in scores:
                file_scores.write(f"{name} {score} ({mode})\n")


class EnemyDown(Exception):
    """Raise this exception when an enemy is destroyed"""


class ExitGame(Exception):
    """Raise this exception when the user wants to exit the game"""

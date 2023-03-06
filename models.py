"""
Сontains the implementation of the Enemy and Player classes for the game.
"""
import random

from exceptions import EnemyDown, GameOver
from settings import PLAYER_LIVES, ALLOWED_ATTACKS


class Enemy:
    """
    A class representing an enemy in the game.
    """
    def __init__(self, level):
        """
        Initializes a new instance of the Enemy class.
        """
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """
        Selects a random attack for the enemy.
        """
        return random.randint(1, 3)

    def decrease_lives(self):
        """
        Decreases the number of lives of the enemy by 1.
        Raises an EnemyDown exception if the enemy has no lives left.
        """
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player:
    """
    A class representing a player in the game.
    """
    def __init__(self, name, game_mode):
        """
        Initializes a new instance of the Player class.
        """
        self.name = name
        self.lives = PLAYER_LIVES
        self.score = 0
        self.allowed_attacks = ALLOWED_ATTACKS
        self.game_mode = game_mode

    @staticmethod
    def fight(attack, defense):
        """
        Determines the result of a fight between an attack and a defense.
        """
        if attack == defense:
            return 0
        if attack == 1 and defense == 3:
            return 1
        if attack == 2 and defense == 1:
            return 1
        if attack == 3 and defense == 2:
            return 1
        return -1

    def decrease_lives(self):
        """
        Decreases the number of lives of the player by 1.
        Raises a GameOver exception if the player has no lives left.
        """
        self.lives -= 1
        if self.lives == 0:
            raise GameOver(self.score, self.name, self.game_mode)
        print(f'Your lives: {self.lives}')

    def attack(self, enemy_obj, mode):
        """
        Performs an attack by the player on the enemy.
        """
        while True:
            try:
                attack = int(input("Choose your attack - wizard(1), warrior(2), or rogue(3): "))
                if attack not in ALLOWED_ATTACKS:
                    raise ValueError("Invalid choice. Please enter a number from 1-3.")
                break
            except ValueError as val:
                print(val)
        defense = enemy_obj.select_attack()
        result = self.fight(attack, defense)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print('You attacked successfully!')
            self.score += (1 * mode)
            print(f'Your score: {self.score}')
            enemy_obj.decrease_lives()
        else:
            print("You missed!")

    def defense(self, enemy_obj):
        """Prompt the player to choose a defense and fight the enemy.
        Update the player's lives accordingly.
        """
        while True:
            try:
                defense = int(input("Choose your attack - wizard(1), warrior(2), or rogue(3): "))
                if defense not in ALLOWED_ATTACKS:
                    raise ValueError("Invalid choice. Please enter a number from 1-3.")
                break
            except ValueError as val:
                print(val)
        attack = enemy_obj.select_attack()
        result = self.fight(attack, defense)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("Enemy attacked successfully!")
            self.decrease_lives()
        else:
            print("Enemy missed!")

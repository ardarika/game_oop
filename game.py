"""
Сontains the main game logic for a text-based RPG game.
It uses models and exceptions modules to create player and enemy objects, and handle exceptions.

The game can be played by running the 'play' function.
Players can choose their game mode (normal/hard),
enter their name, and attack and defend against enemies.
The game ends when the player's lives reach zero or the player defeats all enemies.

The following commands are available during the game: start, show scores, help and exit.

The game saves the final score of the player in a file named 'scores.txt' upon completion.

This module requires the following modules: exceptions, models, and settings.
"""

import sys
import exceptions
import models

from settings import COMMANDS, HARD_MODE_MULTIPLIER


def get_game_mode():
    """
    Asks the user to input a game mode.
    Returns the selected game mode in lowercase.
    """
    while True:
        mode = input('Enter game mode (Normal/Hard): ').strip()
        if mode.lower() in ('normal', 'hard'):
            return mode.lower()
        print('Invalid game mode. Enter "Normal" or "Hard".')


def show_scores():
    """
    Reads and displays scores from the scores.txt file.
    """
    with open('scores.txt', 'r', encoding='utf-8') as scores_file:
        print(scores_file.read())


def exit_game():
    """
    Exits the game by raising an ExitGame exception.
    """
    print('Exiting game...')
    sys.exit()


def menu():
    """
    Displays the game menu.
    """
    print('START | SHOW SCORES | HELP | EXIT')


def play():
    """
    The main function of the game. Allows the player to play the game.
    """
    print('Welcome to the best game ever!\nInput START for start game or HELP for show menu: ')
    while True:
        try:
           command = input('Enter your choice: ')
            if command.lower() == 'exit':
                exit_game()
            elif command.lower() == 'show scores':
                show_scores()
            elif command.lower() == 'start':
                break
            elif command.lower() == 'help':
                menu()
            elif command not in COMMANDS:
                print('Invalid command.')
            else:
                return command
        except exceptions.ExitGame:
            pass

    name = input('Enter your name: ')
    while not name.isalpha():
        print('Invalid input. Name should only contain letters.')
        name = input('Enter your name: ')

    if get_game_mode() == 'hard':
        game_mode = 'hard'
        lives_multiplier = HARD_MODE_MULTIPLIER
        score_multiplier = HARD_MODE_MULTIPLIER
    else:
        game_mode = 'normal'
        lives_multiplier = 1
        score_multiplier = 1

    player = models.Player(name, game_mode)
    level = 1
    enemy = models.Enemy(lives_multiplier)
    print(f'LEVEL {level}\nYour lives: {player.lives}\nEnemy lives: {lives_multiplier}')

    while True:
        try:
            player.attack(enemy, score_multiplier)
            player.defense(enemy)
        except exceptions.EnemyDown:
            player.score += (5 * score_multiplier)
            level += 1
            enemy = models.Enemy(lives_multiplier)
            print(f'LEVEL {level}')
            print(f'Your lives: {player.lives}\nEnemy lives: {level * lives_multiplier}')


if __name__ == '__main__':
    try:
        play()
    except exceptions.GameOver as e:
        e.save_score()
        print(f'Game Over! Your final score is {e.score}')
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye!')

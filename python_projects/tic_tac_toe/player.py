import random
import math


class Player:
    def __init__(self, letter) -> None:
        self.letter = letter

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class RandomComputerPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8)')
            try:
                val = int(square)
                if val not in game.available_move():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid Square. Try again')
        return val


# `player = Player()
# print(player.get_move())`

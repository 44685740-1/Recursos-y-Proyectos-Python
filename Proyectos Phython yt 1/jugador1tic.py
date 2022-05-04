import math
import random

from juegotictactoe import TicTacToe

class player:
    def __init__(self,letter) -> None:
        #letra puede ser x or o
        self.letter = letter

    #queremos que todos los jugadores pasen al siguiente movimiento dado por el juego
    def get_move(self, game):
        pass

class RamdomComputerPlayer(player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
#use TicTacToe porque ahi es donde se definio la clase
    def get_move(self, game):
        square = random.choice(TicTacToe.avaible_Moves)
        return square


class HumanPlayer(player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game):
        valid_squere = False
        val = None
        while not valid_squere:
            square = imput(self,letter + "/" turn )
    

    
class TicTacToe:
    def __init__(self) -> None:
        self.board = [" " for _ in range(9) ] #usaremos una sola lista para representar la tabla 3x3
        self.current_Winner = None #hacer seguimiento del ganador del juego
    
    def Print_board(self):
       for row  in [ self . board [ i * 3 :( i + 1 ) *  3 ] for  i  in  range ( 3 )]:
            print ( '|'  +  '|' . unirse ( row ) +  '|' )

@staticmethod
def print_Boards_Nums():
    # 0 / 2 / 3 nos dice que nuemro pertenece a esa caja
    number_board = [[str(i) for i in range (j*3, (j+1)*3)] for j in range (3)]
    for row in number_board:
        print ( '|'  +  '|' . unirse ( row ) +  '|' )
#ver variable
def avaible_Moves(self):
    return [i for i, spot in enumerate(self,print_Boards_Nums) if spot == " "]


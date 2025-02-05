class Tablero:
  def __init__(self, filas, columnas):
    self._board = self.build_board(filas, columnas)

  def build_board(self, filas, columnas):
    board = []
    for _ in range(filas):
        board.append(["-"] * columnas)
    
    return board
  
  def print_board(self):
    print("#########################")
    print("######### RAYA ##########")
    print("#########################")
    print("1   2   3   4   5   6   7")
    for fila in self._board:
        print("   ".join(fila))

board = Tablero(6, 7)

board.print_board()
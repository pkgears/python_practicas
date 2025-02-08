# Mixin para imprimir mensajes
class Mensaje:
  def imprimir_mensaje(self, texto, simbolo = "*", times = 30):
    bar = f"{simbolo*times}"
    text = texto.center(times)
    print(bar)
    print(text)
    print(bar)

class Tablero:
  DIRECCIONES = [
      {"x": 1, "y": 0}, # derecha
      {"x": 1, "y": -1}, # derecha y abajo
      {"x": 0, "y": -1}, # abajo
      {"x": -1, "y": -1}, # izquierda y abajo
      {"x": -1, "y": 0}, #izquierda
      {"x": -1, "y": 1}, # izquierda y arriba
      {"x": 0, "y": 1}, # arriba
      {"x": 1, "y": 1} # izquierda y arriba
    ]

  def __init__(self, filas, columnas):
    self._board = self.build_board(filas, columnas)
  
  def board(self):
    return self._board

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
  
  def verificar_ganador(self, casilla, jugada, jugador):
    for direccion in self.DIRECCIONES:
      col = casilla + direccion["x"]
      row = jugada + direccion["y"]
      ganador = self.validar_siguiente(jugador, col , row, direccion["x"], direccion["y"])
      if ganador:
        return True
  
    return False

  def validar_siguiente(self, jugador, fila, columna, dir_x, dir_y, contador = 1):
    try:
      if self._board[fila][columna] == jugador:
        contador += 1
        if contador == 4:
          return True
        else:
          fila = fila + dir_x
          columna = columna + dir_y
          return self.validar_siguiente(jugador, fila, columna, dir_x, dir_y, contador)
      else:
        return False
    except IndexError:
      return False


class Juego(Mensaje):
  def __init__(self):
    self._tablero = Tablero(6, 7)
    self._jugadores = {1: "X", 2: "O"}

  def board(self):
    return self._tablero.board()
    
  def iniciar(self):
    self._tablero.print_board()
    turno = 1
    ganador = False
    while True:
      self.imprimir_mensaje(f"Turno del jugador {self._jugadores[turno]}")
      ganador = self.jugar(self._jugadores[turno])

      if ganador is True:
        self.imprimir_mensaje(f"Felicidades", "!")
        self.imprimir_mensaje(f"El jugador {self._jugadores[turno]} ha ganado")
        break

      turno = 1 if turno == 2 else 2

  def jugar(self, jugardor):
    jugada = self.obtener_jugada()
    ganador = self.insertar_ficha(jugada, jugardor)
    self._tablero.print_board()

    return ganador

  def obtener_jugada(self):
    try:
      jugada = input("Ingrese la columna donde desea jugar: ")
      jugada = int(jugada) - 1

      if(jugada < 0 or jugada > 6):
        raise ValueError
      else:
        return jugada
    except ValueError:
      self.imprimir_mensaje("Por favor ingrese un número entre 1 y 7",)
      return self.obtener_jugada()
  
  def insertar_ficha(self, jugada, jugador):
    for casilla in range(len(self.board()), 0, -1):
      casilla = casilla - 1
      if casilla == 0 and self.board()[casilla][jugada] != "-":
        self.imprimir_mensaje("Columna llena, intenta en otra")

        jugada = self.obtener_jugada()
        return self.insertar_ficha(self._tablero, jugada, jugador)

      if self.board()[casilla][jugada] == "-":
          self.board()[casilla][jugada] = jugador
          return self._tablero.verificar_ganador(casilla, jugada, jugador)
      

### Iniciando juego 
juego = Juego()
juego.iniciar()
def crear_tablero():
    tablero = []
    for _ in range(6):
        tablero.append(["-"] * 7)
    
    return tablero

def imprimir_tablero(tablero):
    print("#########################")
    print("######### RAYA ##########")
    print("#########################")
    print("1   2   3   4   5   6   7")
    for fila in tablero:
        print("   ".join(fila))

def obtener_jugada():
  try:
    jugada = input("Ingrese la columna donde desea jugar: ")
    jugada = int(jugada) - 1

    return jugada
  except ValueError:
    imprimir_mensaje("Por favor ingrese un número entre 1 y 7", "*")
    return obtener_jugada()

def insertar_ficha(tablero, jugada, jugador):
  for casilla in range(len(tablero), 0, -1):
    casilla = casilla - 1
    if casilla == 0 and tablero[casilla][jugada] != "-":
      imprimir_mensaje("Columna llena, intenta en otra", "*")

      jugada = obtener_jugada()
      return insertar_ficha(tablero, jugada, jugador)

    if tablero[casilla][jugada] == "-":
        tablero[casilla][jugada] = jugador
        return verificar_ganador(tablero, casilla, jugada, jugador)
  
  
def verificar_ganador(tablero, casilla, jugada, jugador):
  direcciones = [
    {"x": 1, "y": 0}, # derecha
    {"x": 1, "y": -1}, # derecha y abajo
    {"x": 0, "y": -1}, # abajo
    {"x": -1, "y": -1}, # izquierda y abajo
    {"x": -1, "y": 0}, #izquierda
    {"x": -1, "y": 1}, # izquierda y arriba
    {"x": 0, "y": 1}, # arriba
    {"x": 1, "y": 1} # izquierda y arriba
  ]

  for direccion in direcciones:
    col = casilla + direccion["x"]
    row = jugada + direccion["y"]
    ganador = validar_siguiente(tablero, jugador, col , row, direccion["x"], direccion["y"])
    if ganador:
      return True
  
  return False


def validar_siguiente(tablero, jugador, fila, columna, dir_x, dir_y, contador = 1):
  try:
    if tablero[fila][columna] == jugador:
      contador += 1
      if contador == 4:
        return True
      else:
        fila = fila + dir_x
        columna = columna + dir_y
        return validar_siguiente(tablero, jugador, fila, columna, dir_x, dir_y, contador)
    else:
      return False
  except IndexError:
    return False

def imprimir_mensaje(texto, simbolo, times = 30):
  print(f"{simbolo*times}")
  print(f"{simbolo*3} {texto} {simbolo*3}")
  print(f"{simbolo*times}")


def jugar():
  tablero = crear_tablero()
  imprimir_tablero(tablero)

  jugadores = {1: "X", 2: "O"}
  turno = 1

  ganador = None

  while True:

    imprimir_mensaje(f"Turno del jugador {jugadores[turno]}", "*")
    jugada = obtener_jugada()
    
    ganador = insertar_ficha(tablero, jugada, jugadores[turno])

    imprimir_tablero(tablero)
    if ganador is True:
      imprimir_mensaje(f"El jugador {jugadores[turno]} ha ganado", "*")
      break

    turno = 1 if turno == 2 else 2

jugar()
from turtle import Terminator, Turtle
from time import sleep
from board import Board

class SnakeGame():
  START_TEXT = "Presiona espacio para iniciar o Q para salir"
  GAME_OVER_TEXT = "Game Over"

  def __init__(self):
    self.score = 0
    self.scoreRecord = 0
    self.playing = False
    
    self.board = Board()
    self.board.screen.onkey(self.play, "space")
    self.board.screen.onkey(self.board.screen.bye, "q")
    
    self.infoText = Turtle()
    self.showStartGameText()

  def showStartGameText(self):
    self.infoText.hideturtle()
    self.infoText.color("white")
    self.infoText.penup()
    self.infoText.goto(0, 230)
    self.infoText.write(self.START_TEXT, align="center", font=("Arial", 16, "normal"))

  def showGameOverText(self):
    self.infoText.goto(0, 80)
    self.infoText.write(self.GAME_OVER_TEXT, align="center", font=("Arial", 16, "normal"))
  
  def play(self):
    self.playing = True
    self.infoText.clear()
    self.infoText.goto(0, 230)
    self.board.resetBoard()
  
  def gameOver(self):
    self.playing = False
    self.infoText.clear()
    self.showStartGameText()
    self.showGameOverText()
    
  def startGame(self):
    try:
      while True:
        if self.playing:
          self.board.moveSnake()
          if self.board.snakeCrash():
            self.gameOver()

        self.board.updateScreen()

        sleep(0.1)
    except KeyboardInterrupt:
        print("Cerrando el juego...")
        self.screen.bye()
    except Terminator:
        print("El juego ha cerrado.")
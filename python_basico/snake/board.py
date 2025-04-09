from turtle import Screen, Turtle
from snake import Snake
from food import Food

class Board:
  
  def __init__(self):
    self._score = 0
    self._scoreRecord = 0

    self.screen = Screen()
    self._food = None

    self._scoreBoard = Turtle()
    self._snake = Snake()

    self._screenSetup()
    self._scoreSetup()
    self._listenSnakeMove()
    

  def resetBoard(self):
    self._resetSnake()
    self._resetFood()
    self._score = 0
    self._updateScore()

  def moveSnake(self):
    self._snake.move()
    if(self._snake.head.distance(self._food.fruit()) < 15):
      self._food.refresh()
      self._snake.add_segment()
      self._score += 1
      if self._score > self._scoreRecord:
        self._scoreRecord = self._score
      self._updateScore()
  
  def snakeCrash(self):
    return self._snake.crash()
  
  def updateScreen(self):
    self.screen.update()

  # private methods  

  def _screenSetup(self):
    self.screen.setup(width=600, height=600)
    self.screen.title("Snake Game")
    self.screen.bgcolor("green")
    self.screen.tracer(0)
    
    self.screen.listen()
  
  def _scoreSetup(self):
    self._scoreBoard.hideturtle()
    self._scoreBoard.color("white")
    self._scoreBoard.penup()
    self._scoreBoard.goto(0, 260)
    self._scoreBoard.write("Hola", align="center", font=("Arial", 16, "normal"))

  def _scoreText(self):
    return f"Score: {self._score} Record: {self._scoreRecord}"
  
  def _listenSnakeMove(self):
    self.screen.onkey(self._snake.up, "Up")
    self.screen.onkey(self._snake.down, "Down")
    self.screen.onkey(self._snake.left, "Left")
    self.screen.onkey(self._snake.right, "Right")
  
  def _resetSnake(self):
    self._snake.destroy()
    self._snake.create_snake()

  def _resetFood(self):
    if self._food:
      self._food.destroy()
    self._food = Food()
    self._food.refresh()

  def _updateScore(self):
    self._scoreBoard.clear()
    self._scoreBoard.write(self._scoreText(), align="center", font=("Arial", 16, "normal"))

  
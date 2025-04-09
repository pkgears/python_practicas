import random
from turtle import Turtle

class Food():
  def __init__(self):
    self.food = Turtle("circle")
    self.food.color("red")
    self.food.penup()
    self.food.speed(0)
    self.refresh()

  def refresh(self):
    x, y = self._generateCords(), self._generateCords()
    self.food.goto(x,y)
  
  def fruit(self):
    return self.food
  
  def destroy(self):
    self.food.goto(1000, 1000)
    self.food.clear()
    
  def _generateCords(self):
    return random.randint(-14, 11) * 20

from turtle import Turtle

class Snake:
  def __init__(self):
    self.segments = []
    self.head = None
    self.create_snake()

  def create_snake(self):
    for i in range(3):
      self.add_segment()
    self.head = self.segments[0]

  def add_segment(self):
    new_segment = Turtle("square")
    new_segment.color("black")
    new_segment.penup()
    if len(self.segments) > 0:
      x = self.segments[-1].xcor() - 20
      y = self.segments[-1].ycor()
      new_segment.goto(x, y)
    else:
        new_segment.color("white")
        new_segment.goto(20, 0)
    self.segments.append(new_segment)

  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
      x = self.segments[seg_num - 1].xcor()
      y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(x, y)
    self.head.forward(20)
  
  def up(self):
    if self.head.heading() != 270:
      self.head.setheading(90)

  def down(self):
    if self.head.heading() != 90:
      self.head.setheading(270)

  def left(self):
    if self.head.heading() != 0:
      self.head.setheading(180)

  def right(self):
    if self.head.heading() != 180:
      self.head.setheading(0)
    
  def crash(self):
    return self._bodyCrash() or self._wallCash()
  
  def destroy(self):
    for segment in self.segments:
      segment.goto(1000, 1000)
    self.segments.clear()

  ## Private methods

  def _bodyCrash(self):
    for segment in self.segments[1:]:
      if self.head.distance(segment) < 10:
        return True
    return False
  
  def _wallCash(self):
    if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 240 or self.head.ycor() < -290:
      return True
    return False
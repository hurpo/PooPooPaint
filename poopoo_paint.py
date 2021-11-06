import turtle as trtl #Importing Turtrle
import math
size = 5
turtle_size = 1
wn = trtl.Screen()
pen = trtl.Turtle()
pen.shape("circle")
pen.turtlesize(turtle_size)
pen.pensize(size)
pen.speed(0)
#Setting up screen size
wn.setup(750,750)

#Makes place for colors and tools to be 
paint_holder = trtl.Turtle()
paint_holder.hideturtle()
paint_holder.color("Tan")
paint_holder.speed(0)
paint_holder.penup()
paint_holder.goto(-400,-270)
paint_holder.pendown()
paint_holder.begin_fill()
for i in range(4):
  paint_holder.forward(800)
  paint_holder.right(90)
paint_holder.end_fill()

#Func for clearing the page
def clear_page(x,y):
  pen.clear()

#Func for increasing pen size
def increase_size(x,y):
  global size
  global turtle_size
  size += 5
  turtle_size += .25
  pen.turtlesize(turtle_size)
  pen.pensize(size)

#Func for decreasing pen size
def decrease_size(x,y):
  global size
  global turtle_size
  if turtle_size > 1:
      size -= 5
      turtle_size -= .25
  pen.turtlesize(turtle_size)
  pen.pensize(size)

#All this funcs change the color of the pen
def turn_blue(x, y):
  pen.color("Blue")
def turn_green(x, y):
  pen.color("Green")
def turn_red(x, y):
  pen.color("red")
def turn_black(x, y):
  pen.color("black")
def turn_white(x, y):
  pen.color("white")
def turn_yellow(x, y):
  pen.color("yellow")
def turn_orange(x, y):
  pen.color("orange")
def turn_cyan(x, y):
  pen.color("cyan")
def turn_purple(x, y):
  pen.color("purple")
def turn_pink(x, y):
  pen.color("pink")
making_lines = False

#Turns on the line tool
def go_line(x,y):
  #the global is there so I can use vars defined outside the function

  #the making lines makes is a flag to change how a function later in the code works
  global making_lines

  #the line clicked var is so the line doesnt start on the button
  global line_clicked
  if making_lines:
      line.color("Black")
      making_lines = False
      line_clicked = 0
  else:
      line.color("White")
      making_lines = True
making_box = False

#Func to make box
def go_box(x,y):
  global making_box
  global box_clicked
  if making_box:
      box.color("Black")
      making_box = False
      box_clicked = 0
  else:
      box.color("White")
      making_box = True
making_circle = False

# func makes circle
def go_circle(x,y):
  global making_circle
  global circle_clicked
  if making_circle:
     circle.color("Black")
     making_circle = False
     circle_clicked = 0
  else:
     circle.color("White")
     making_circle = True
paint_height = -315

#each of these chunks of code defines a new turtle, that are used as buttons
clear = trtl.Turtle()
clear.penup()
clear.goto(-340,paint_height)
clear.setheading(90)
clear.shape("turtle")
clear.turtlesize(2)
clear.color("Red")
#the on click method checks if the turtle is clicked, and puts its cords into a func, but idc about the cords just that it calls a func
clear.onclick(clear_page)

increase = trtl.Turtle()
increase.penup()
increase.goto(-270,paint_height + 10)
increase.shape("arrow")
increase.turtlesize(2)
increase.setheading(90)
increase.color("black")
increase.onclick(increase_size)

decrease = trtl.Turtle()
decrease.penup()
decrease.goto(-270,paint_height - 10)
decrease.shape("arrow")
decrease.turtlesize(2)
decrease.setheading(-90)
decrease.color("black")
decrease.onclick(decrease_size)

blue = trtl.Turtle()
blue.penup()
blue.goto(-200,paint_height)
blue.shape("circle")
blue.turtlesize(2)
blue.color("blue")
blue.onclick(turn_blue)

green = trtl.Turtle()
green.penup()
green.goto(-150,paint_height)
green.shape("circle")
green.turtlesize(2)
green.color("green")
green.onclick(turn_green)

red = trtl.Turtle()
red.penup()
red.goto(-100,paint_height)
red.shape("circle")
red.turtlesize(2)
red.color("red")
red.onclick(turn_red)

black = trtl.Turtle()
black.penup()
black.goto(-50,paint_height)
black.shape("circle")
black.turtlesize(2)
black.color("black")
black.onclick(turn_black)

white = trtl.Turtle()
white.penup()
white.goto(0,paint_height)
white.shape("circle")
white.turtlesize(2)
white.color("white")
white.onclick(turn_white)

yellow = trtl.Turtle()
yellow.penup()
yellow.goto(50,paint_height)
yellow.shape("circle")
yellow.turtlesize(2)
yellow.color("yellow")
yellow.onclick(turn_yellow)

orange = trtl.Turtle()
orange.penup()
orange.goto(100,paint_height)
orange.shape("circle")
orange.turtlesize(2)
orange.color("orange")
orange.onclick(turn_orange)

cyan = trtl.Turtle()
cyan.penup()
cyan.goto(150,paint_height)
cyan.shape("circle")
cyan.turtlesize(2)
cyan.color("cyan")
cyan.onclick(turn_cyan)

purple = trtl.Turtle()
purple.penup()
purple.goto(200,paint_height)
purple.shape("circle")
purple.turtlesize(2)
purple.color("purple")
purple.onclick(turn_purple)

pink = trtl.Turtle()
pink.penup()
pink.goto(250,paint_height)
pink.shape("circle")
pink.turtlesize(2)
pink.color("pink")
pink.onclick(turn_pink)

line = trtl.Turtle()
line.penup()
line.goto(305,paint_height + 10)
line.shape("classic")
line.turtlesize(2)
line.color("Black")
line.onclick(go_line)

box = trtl.Turtle()
box.penup()
box.goto(335,paint_height + 10)
box.shape("square")
box.turtlesize(1)
box.color("Black")
box.onclick(go_box)

circle = trtl.Turtle()
circle.penup()
circle.goto(315,paint_height - 12)
circle.shape("circle")
circle.turtlesize(1)
circle.color("Black")
circle.onclick(go_circle)

#This actually creates the box
def calc_box(x_2, y_2, x_1, y_1):
  print("In here")
  dist_x = x_2 - x_1
  dist_y = y_2 - y_1
  pen.setheading(90)
  for i in range(2):
      pen.pendown()
      pen.forward(dist_y)
      pen.right(90)
      pen.forward(dist_x)
      pen.right(90)
      pen.penup()

#This actually creates the circle, tried using calculus to make it better but im exhausted
def calc_circle(x_1,y_1,x_2,y_2):

  #We calc the distance from the intial pos between the pos clicked on to get radius
  x_leng = x_2 - x_1
  y_leng = y_2 - y_1
  c_length = math.sqrt( pow(x_leng, 2) + pow(y_leng, 2) )
  radius = c_length /2

  pen.pendown()

  #draws circle above second click with radius calcuated above (sometimes)
  pen.circle(radius)
  pen.setheading(0)
  pen.penup()
  #pen.setheading(0)
  print("Start", x_1, y_1, "Finish", x_2, y_2)
  #print(c_length, radius, math.degrees(angle_at_start))

storedx = pen.xcor()
storedy = pen.ycor()

line_started = False
line_clicked = 0

box_started = False
box_clicked = 0

circle_started = False
circle_clicked = 0

#places the turtle where you click, but if the line, circle, or box tool are on, it do that crap instead
def go_to(x,y):
  linex = pen.xcor()
  liney = pen.ycor()
  boxx = pen.xcor()
  boxy = pen.ycor()
  circlex = pen.xcor()
  circley = pen.ycor()
  if making_lines:
      global line_clicked
      line_clicked += 1
      global line_started
      if line_started == False and line_clicked >1:
          pen.penup()
          pen.goto(x,y)
          pen.shape("classic")
          line_started = True
          pen.down()
          pen.goto(linex, liney)
      else:
          pen.shape("square")
          linex = pen.xcor()
          liney = pen.ycor()
          if  line_clicked >1:
              pen.penup()
              pen.goto(x,y)
          line_clicked += 1
          line_started = False
  elif making_box:
      global box_clicked
      box_clicked += 1
      global box_started
      if box_started == False and box_clicked >1:
          pen.penup()
          pen.goto(x,y)
          pen.shape("classic")
          box_started = True
          calc_box(boxx, boxy, pen.xcor(), pen.ycor())
      else:
          pen.shape("square")
          boxx = pen.xcor()
          boxy = pen.ycor()
          print("START", boxx, boxy)
          if  box_clicked >1:
                  pen.penup()
                  pen.goto(x,y)
          box_started = False
  elif making_circle:
      global circle_clicked
      circle_clicked += 1
      global circle_started
      if circle_started == False and circle_clicked >1:
         pen.penup()
         pen.goto(x,y)
         pen.shape("classic")
         circle_started = True
         calc_circle(circlex, circley, pen.xcor(), pen.ycor())
      else:
         pen.shape("square")
         circlex = pen.xcor()
         circley = pen.ycor()
         if  circle_clicked >1:
            pen.penup()
            pen.goto(x,y)
         circle_started = False
  else:
     #this is the code that does the moving the turtle
      pen.shape("circle")
      global storedx
      global storedy
      storedx = pen.xcor()
      storedy = pen.ycor()
      print(storedx, storedy)
      pen.penup()
      pen.goto(x,y)
      pen.pendown()
      pen.ondrag(drag_pen)

#this func is so you can drag the cursor
def drag_pen(x,y):
  if y > -270:
      pen.ondrag(None)
      pen.goto(x,y)
      pen.ondrag(drag_pen)
wn.onscreenclick(go_to)
pen.ondrag(drag_pen)
wn.mainloop()
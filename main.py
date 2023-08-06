import turtle
import random
TRACK_X=-350
TRACK_Y=200
TRACK_LEN=700
TRACK_WIDTH=400
LANE_WIDTH = 100
LANE_NUMBER_X = -380
LANE_NUMBER_Y = 130
FINISH_X = 250
TURTLE_X, TURTLE_Y = -300, 150
def setup_screen():
  global turt, screen
  
  screen = turtle.getscreen()
  screen.setup(800,500)
  screen.title("The Young Maker - Racing Turtle")
  screen.bgcolor("#9F4123")

  turt = turtle.getturtle()
  turt.speed(0)
  turt.penup()
  turt.goto(-100, 205)
  turt.color("white")
  turt.write("Racing Turtles", font=("Arial", 20,"bold"))

  draw_track()
  draw_finishline()
  

def draw_track():
  turt.goto(TRACK_X,TRACK_Y)
  turt.pendown()
  turt.color("chocolate")
  turt.begin_fill()
  for i in range(2):
    turt.forward(TRACK_LEN)
    turt.right(90)
    turt.forward(TRACK_WIDTH)
    turt.right(90)

  turt.end_fill()

  turt.color("white")
  for index in range(5):
    turt.penup()
    turt.goto(TRACK_X, TRACK_Y - LANE_WIDTH * index)
    turt.pendown()
    turt.forward(TRACK_LEN)

  turt.penup()
  for index in range(4):
    turt.goto(LANE_NUMBER_X, LANE_NUMBER_Y - LANE_WIDTH * index)
    turt.write(index+ 1, font=("Arial", 20, "bold" ))
  
def draw_finishline():
  turt.penup()
  turt.goto(FINISH_X, TRACK_Y)
  turt.right(90)
  turt.pendown()
  turt.width(10)
  turt.forward(TRACK_WIDTH)

def setup_turtles():
  global turtle1, turtle2, turtle3, turtle4
  turtle1 = turtle.Turtle()
  turtle2 = turtle.Turtle()
  turtle3 = turtle.Turtle()
  turtle4 = turtle.Turtle()

  global turtlelist
  turtlelist = [turtle1, turtle2, turtle3, turtle4]
  colorlist = ["lightblue", "pink", "red", "green"]

  for i in range(4):
    currturt = turtlelist[i]
    currturt.penup()
    currturt.color(colorlist[i])
    currturt.shape("turtle")
    currturt.turtlesize(2)
    currturt.goto(TURTLE_X, TURTLE_Y - LANE_WIDTH * i)
    currturt.pendown()



def get_userguess():
  return screen.numinput("Guess!","which turtle will win? ( 1, 2, 3 or 4)",
                         minval=1,
                         maxval=4)

def race(user_guess: int):
  while (turtle1.xcor()<= FINISH_X and
         turtle2.xcor()<= FINISH_X and
         turtle3.xcor()<= FINISH_X and
         turtle4.xcor()<= FINISH_X):
          turtle1.forward(random.randint(1, 10))
          turtle2.forward(random.randint(1, 10))
          turtle3.forward(random.randint(1, 10))
          turtle4.forward(random.randint(1, 10))
          if turtle1.xcor() > FINISH_X:
            winner = 1
          elif turtle.xcor() > FINISH_X:
            winner = 2
          elif turtle.xcor() > FINISH_X:
            winner = 3
          elif turtle.xcor() > FINISH_X:
            winner = 4
  if(user_guess == winner):
    screen.textinput("Game over",
                    "You win! Turtle" + str(winner) + "won the game")
  else:
    screen.textinput("Game over!",
                    "You lose! Turtle " + str(winner) + " won the game")
def main():
  setup_screen()
  setup_turtles()
  user_guess = get_userguess()
  race(user_guess)


  
if __name__=="__main__":
  main()





















































































































  
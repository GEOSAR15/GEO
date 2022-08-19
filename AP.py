import turtle  # for graphics
import os
import sys  # the other 4 imports are for end screen/restart
import subprocess
import easygui # for start screen

# start screen for the game
yn1 = easygui.ynbox('Instructions: Get through the maze to the red square\nControls: W - up S - down D - right '
                    'a - left\n\nStart game?', 'START?', ['Yes', 'No'])
if yn1 != True:
    exit()

win = turtle.Screen()  # setup for the window
win.setup(800, 700)
win.title("MAZE")
win.bgcolor("black")


# Creating pen class


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.color("white")
        self.speed(0)


class Endblock(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.color("red")
        self.speed(0)


pen = Pen()


# creating character and movements/ block interaction
class Char(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("turtle")
        self.color("red")
        self.speed(0)

    def up_w(self):  # for up movement
        if (self.xcor(), self.ycor() + 24) not in walls:
            self.goto(self.xcor(), self.ycor() + 24)
        if (self.xcor(), self.ycor() + 24) in endblocks:
            self.goto(1000,1000)
            self.hideturtle()
            endscreen()

    def left_a(self):  # for left movement
        if (self.xcor() - 24, self.ycor()) not in walls:
            self.goto(self.xcor() - 24, self.ycor())
        if (self.xcor() - 24 , self.ycor()) in endblocks:
            self.goto(1000, 1000)
            self.hideturtle()
            endscreen()

    def right_d(self):  # for right movement
        if (self.xcor() + 24, self.ycor()) not in walls:
            self.goto(self.xcor() + 24, self.ycor())
        if (self.xcor() + 24 , self.ycor()) in endblocks:
            self.goto(1000, 1000)
            self.hideturtle()
            endscreen()

    def down_s(self):  # for down movement
        if (self.xcor(), self.ycor() - 24) not in walls:
            self.goto(self.xcor(), self.ycor() - 24)
        if (self.xcor(), self.ycor() - 24) in endblocks:
            self.goto(1000,1000)
            self.hideturtle()
            endscreen()


char = Char()

# List for levels
levels = [""]

# Format for first level
level_1 = [
"NNNNNNNNNNNNNNNNNNNNNNNNNNN",
"NC NNNNNNNNNNNNNNNNNNNNNNNN",
"N               NNNNNNNNNNN",
"N  NNNNNNNNNNN  NNNNNNN  NN",
"NNNNNNN                  NN",
"NNNNNNN  NNNNNNNNNNNNNNNNNN",
"NNNNNNN  NNNNN            N",
"NNNNNNNN        NNNNNNNNNNN",
"NNNNNNN  NNNNNNNNNNNNNNNNNN",
"NNNN                      N",
"N     NNNNNNNNNNNNNNN  NNNN",
"NNNNNNNNNNNNNNNNNNNNN  NNNN",
"NNNNNNNN               NNNN",
"NNNNNNNN   NNNNNNNNNNNNNNNN",
"NNNNNNNN  NNNNNNNNNNNNNNNNN",
"N         NNNNNNNNNNNNNNNNN",
"NNNNNNNN                 EN",
"NNNNNNNN NNNNNNNNNNNNNNNNNN",
"       NNN                 "
]

# adds level_1 to list
levels.append(level_1)

# creates wall list for collision mechanic
walls = []

# creates list for the red block that signals end of maze
endblocks = []

endblock = Endblock()

# for the actual generation of the maze


def mazelvl(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            drawer = maze[y][x]
            screen_x = -300 + (x * 24)
            screen_y = 270 - (y * 24)

            if drawer == "E":
                endblock.goto(screen_x, screen_y)
                endblocks.append((screen_x, screen_y))

            if drawer == "N":
                pen.goto(screen_x, screen_y)
                pen.stamp()

                # adds the coordinates of walls to the walls list
                walls.append((screen_x, screen_y))

            if drawer == "C":
                char.goto(screen_x, screen_y)

# calls mazelvl function
mazelvl(levels[1])

# keybinds for movement
turtle.listen()
turtle.onkey(char.up_w, "w")
turtle.onkey(char.left_a, "a")
turtle.onkey(char.right_d, "d")
turtle.onkey(char.down_s, "s")

# for the end screen input
def endscreen():
    yn = easygui.ynbox('You won, would you like to play again?', 'Continue?', ['Yes', 'No'])
    if yn == True:
        subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
    win.exitonclick()


# to keep the window running
while True:
    win.update()

# Simple connect 4 game using Python 3 and Turtle
# This was kept as simple as possible in 6x7 grid
# It does not self check for a four in a row win
# Jean Joubert 10 Nov 2019

import turtle
import os # winsound for windows

win = turtle.Screen()
win.title('Connect 4 using Python 3 and Turtle')
win.setup(700, 700)
win.bgcolor('black')
win.tracer(0)
win.listen()
piece_list = []

class Tile(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(5, 5)
        self.up()
        self.color('blue')


class Piece(turtle.Turtle):
    def __init__(self, color, state):
        super().__init__(shape='circle')
        self.shapesize(4.5, 4.5)
        self.up()
        self.c = color
        self.color(self.c)
        self.state = state
        

    def move_right(self):
        if self.xcor()<300 and self.state == 'move':
            self.goto(self.xcor()+100, self.ycor())

    def move_left(self):
        if self.xcor()>-300 and self.state =='move':
            self.goto(self.xcor()-100, self.ycor())

    def drop(self):
        global piece_list
        # Create new piece to be dropped
        dropped_piece = turtle.Turtle()
        dropped_piece.shape('circle')
        dropped_piece.shapesize(4.5, 4.5)
        dropped_piece.color(self.c)
        dropped_piece.up()

        # Check drop position in y list
        for i in y_list[::-1]:
            #print(i)

            if (self.xcor(),i) not in piece_list:
                ypos = i
                break
            else:
               
                #print('In the list')
                if (self.xcor(), 200) in piece_list:
                    ypos = 1000  # Hide off screen if column is full
                    print("cannot add to the column")
            
        os.system('afplay drop.wav&') # aplay in linux, winsound in windows                
        dropped_piece.goto(self.xcor(), ypos)
        xcor = dropped_piece.xcor()
        ycor = dropped_piece.ycor()
        
        # Only add to the list if dropped within the grid
        if ycor != 1000:
            piece_list.append((xcor,ycor))
                        
        # Change color of the player piece
        if self.c == 'red':

            self.c = 'yellow'
            self.color(self.c)
        else:
            self.c = 'red'
            self.color(self.c)


x_list = [-300, -200, -100, -0, 100, 200, 300]
y_list = [200, 100, 0, -100, -200, -300]

# Place blue 100x100 background tiles and fill with black circles/pieces
for i in x_list:
    for j in y_list:
        tile = Tile()
        tile.goto(i,j)

        piece = Piece('black', 'still')
        piece.goto(i,j)

# Create player piece - red that will move with left or right keys
piece1 = Piece('red', 'move')
piece1.goto(0, 300)

win.onkey(piece1.move_right, 'Right')
win.onkey(piece1.move_left, 'Left')
win.onkey(piece1.drop, 'space')

game_over = False


while not game_over:
    if len(piece_list) >= 42:
        game_over = True
    win.update()

print("GAME OVER")
pen = turtle.Turtle()
pen.up()
pen.hideturtle()
pen.color('blue')
pen.goto(0, 280
         )
pen.write('GAME OVER', align='center', font=('Courier', 36, 'normal'))



        
   
   
        
        

# Simple connect 4 game using Python 3 and Turtle
# This was kept as simple as possible to teach coding to my kids
# Jean Joubert 10 Nov 2019
# Sound using os and afplay with drop.wav, aplay for linux, winsound for windows or # out code

import turtle
import numpy as np
import os # Mac os - will need winsound in windows


# Create numpy representation of the board
board = np.zeros((5, 6))

# Red will be 1 and Yellow 2 (piece)
def drop_piece(board, row, col, piece):
    board[row][col] = piece


def four_in_row(board,piece):
    # Check all horizontal locations for win
    for c in range(3): # Can't get 4 in row in the last 3 cols
        for r in range(5):
            if board[r][c] == piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True

    # Vertical 
    for c in range(6): # Can't get 4 in row in the last 3 cols
        for r in range(2):
            if board[r][c] == piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True

    # Check positively sloped diagonals
    for c in range(3): # Can't get 4 in row in the last 3 cols
        for r in range(2):
            if board[r][c] == piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True

    # Check negatively sloped diagonals
    for c in range(6): # Can't get 4 in row in the last 3 cols
        for r in range(3, 5):
            if board[r][c] == piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True

            
win = turtle.Screen()
win.title('Connect 4 using Python 3 and Turtle')
win.setup(500, 600)
win.bgcolor('black')
win.tracer(0)
win.listen() #Listen for key presses (left, right, space)

piece_list = [] # To save (x,y) dropped pieces only if in the grid


class Tile(turtle.Turtle): # Tile is a turtle object
    def __init__(self):
        super().__init__(shape='square') # Initialize parent class
        self.shapesize(5, 5) # Stretch from 20x20 to 100x100 or 5x
        self.up() # Lift pen up to avoid drawing with the turtle
        self.color('blue')


class Piece(turtle.Turtle):
    def __init__(self, color, state):
        super().__init__(shape='circle')
        self.shapesize(4.5, 4.5)
        self.up()
        self.c = color # Will be used to change color
        self.color(self.c)
        self.state = state
        

    def move_right(self):
        # Move to next column only if still within the grid
        if self.xcor()<200 and self.state == 'move':
            self.goto(self.xcor()+100, self.ycor())


    def move_left(self):
        if self.xcor()>-200 and self.state =='move':
            self.goto(self.xcor()-100, self.ycor())


    def drop(self):
        global game_over
        global board
        global piece_list # To save (x,y) position after drop
        
        # Create new piece to be dropped
        dropped_piece = turtle.Turtle()
        dropped_piece.shape('circle')
        dropped_piece.shapesize(4.5, 4.5)
        dropped_piece.color(self.c)
        dropped_piece.up()

        # Check drop position in y list from the last element to the first (backwards or -1)
        for i in y_list[::-1]:
            #print(i)
            
            if (self.xcor(),i) not in piece_list:
                ypos = i
                break
            else:
                #print('In the piece list')
                # Column is already full:
                if (self.xcor(), 150) in piece_list:
                    ypos = 1000  # Hide off screen if column is full
                    #print("cannot add to the column")
            
        os.system('afplay drop.wav&') # & added to cont with game, winsound for windows               
        dropped_piece.goto(self.xcor(), ypos)
        xcor = dropped_piece.xcor()
        ycor = dropped_piece.ycor()
        
        # Only add to the list if dropped within the grid
        if ycor != 1000:
            piece_list.append((xcor,ycor))
                        
        # Change color of the player piece
        if self.c == 'red':
            piece = 1

            self.c = 'yellow'
            self.color(self.c)
        else:
            self.c = 'red'
            self.color(self.c)
            piece = 2

        # Drop in numpy grid using index positions and the piece (red = 1 and yellow=2)
        drop_piece(board, x_list.index(xcor), y_list.index(ycor), piece)
        #print(board)

        # Check winning move
        if four_in_row(board,1) or four_in_row(board,2):
            win.update()
            game_over = True


x_list = [-200, -100, -0, 100, 200]
y_list = [150, 50, -50, -150, -250]

# Place blue 100x100 background tiles and fill with black circles/pieces
for i in x_list:
    for j in y_list:
        tile = Tile()
        tile.goto(i,j)

        piece = Piece('black', 'still')
        piece.goto(i,j)

# Create player piece - red that will move with left or right keys
piece1 = Piece('red', 'move')
piece1.goto(0, 250)

win.onkey(piece1.move_right, 'Right')
win.onkey(piece1.move_left, 'Left')
win.onkey(piece1.drop, 'space')

game_over = False


# MAIN GAME LOOP:
while not game_over:
    if len(piece_list) >= 25:
        game_over = True
    win.update()


# GAME OVER
print("GAME OVER")
pen = turtle.Turtle()
pen.up()
pen.hideturtle()
pen.color('blue')
pen.goto(0, 220)
pen.write('GAME OVER', align='center', font=('Courier', 36, 'normal'))



        
   
   
        
        

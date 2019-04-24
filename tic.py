# == Jacob Bryant == #
# == Tic Tac Toe  == #

from tkinter import font
import tkinter as tk
import time

# -- Global variables -- #
bsize = 9 # Size of board (3 x 3 = 9)

# -- Player class which keeps track of player abilities and variables -- #
class Player:
    def __init__(self, player):
        self.turn = True if player is 1 else False
        self.symbol = 'X' if player is 1 else 'O'


# -- Graphics code is here -- #
class App(tk.Frame):
    # -- Define the player variables -- #
    player1 = Player(1)
    player2 = Player(2)

    # -- Define the game state data structures -- #
    squares = {} # Keeps track of filled squares by their number
    game_state = True
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_board()

    def create_board(self):
        # -- Generate the board
        board = tk.Frame(root, pady=10, bg="#ffcfe2")
        board.pack()

        # -- Label to keep track of player turn
        text_font = font.Font(family="Helvetica", size=20)
        turn_label = tk.Label(root, text="Player 1's Turn", font=text_font, bg="#ffcfe2", width=60, height=60)
        turn_label.pack()

        # -- Populate board with boxes
        x = 0
        box = []
        text_font = font.Font(family="Helvetica", size=12)
        for y in range(0, bsize):
            if(y % 3 is 0 and y is not 0):
                x+=1

            # -- Add new box to the grid and place it in the box array
            box.append(tk.Button(board, text=" ", font=text_font, bg="Powder Blue", width=winx//(winx//10), height=winy//(winy//8), command=lambda y=y:self.box_click(box_hit=box[y], turn_hit=turn_label, cell_num=y, boxes=box)))
            box[y].grid(row=x%3, column=y%3)
            
    def box_click(self, box_hit, turn_hit, cell_num, boxes):
        current_player = "" # Player that clicked cell

        if(self.game_state is True):
            if(box_hit["text"] is " "): # If the cell is empty
                # -- Find player's turn, change the turn, and then fill the squares dictonary with used cell -- #
                if(self.player1.turn is True):
                    bsymbol = current_player = self.player1.symbol
                    
                    self.player1.turn = False
                    self.player2.turn = True
                    self.squares[cell_num] = self.player1.symbol
                    
                    turn_hit["text"] = "Player 2's Turn"
                else:
                    bsymbol = current_player = self.player2.symbol
                    
                    self.player1.turn = True
                    self.player2.turn = False
                    self.squares[cell_num] = self.player2.symbol
                    
                    turn_hit["text"] = "Player 1's Turn"

                box_hit["text"] = current_player # Change symbol on the cell to the player's symbol
                
                # -- Check to see if any of the players have won -- #

                # -- Fill array is the array of cells that current player has
                fill = []
                for key, val in self.squares.items():
                    if(val is current_player):
                        fill += [key]

                # -- Check for winning or tieing conditions
                if((0 in fill and 1 in fill and 2 in fill) or (3 in fill and 4 in fill and 5 in fill) or (6 in fill and 7 in fill and 8 in fill)): # Horizontal
                    turn_hit["text"] = "Player %s wins!\nClick any cell to restart." % (current_player)
                    self.game_state = False
                elif((0 in fill and 3 in fill and 6 in fill) or (1 in fill and 4 in fill and 7 in fill) or (2 in fill and 5 in fill and 8 in fill)): # Vertical
                    turn_hit["text"] = "Player %s wins!\nClick any cell to restart." % (current_player)
                    self.game_state = False
                elif((0 in fill and 4 in fill and 8 in fill) or (2 in fill and 4 in fill and 6 in fill)): # Diagonal
                    turn_hit["text"] = "Player %s wins!\nClick any cell to restart." % (current_player)
                    self.game_state = False
                elif(len(self.squares) is bsize): # Players tie (Means none of the other winning conditions were true but size of used square dictionary is equal to size of board)
                    turn_hit["text"] = "Tie!\nClick any cell to restart."
                    self.game_state = False
            else: # If the cell is not empty
                # -- If cell is alread in use, do not change player's turn
                if(self.player1.turn is True):
                    turn_hit["text"] = "Player 1's Turn"
                else:
                    turn_hit["text"] = "Player 2's Turn"
        else: # -- Reset game
            self.game_state = True
            for i in boxes:
                i["text"] = " "

            self.squares = {}
                
            turn_hit["text"] = "Player 1's Turn"
            self.player1.turn = True
            self.player2.turn = False
            
            
# -- Define the main window -- #
root = tk.Tk()

winx=600 # Width of window
winy=600 # height of window

ws = root.winfo_screenwidth() # Width of the screen
hs = root.winfo_screenheight() # Height of the screen
# -- Calculate the x and y coordinates of the Tk root window
x = (ws/2) - (winx/2)
y = (hs/2) - (winy/2)

root.geometry("%dx%d+%d+%d" % (winx,winy, x, y)) # Window size

root.config(background="#ffcfe2")
root.resizable(False, False)
root.title("Tic Tac Toe")

# -- Start the app here -- #
app = App(master=root)
app.mainloop()

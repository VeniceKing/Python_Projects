from random import randint

board = []

s = input("How hard is the board?")

for x in range(0, int(s)):
  board.append(["O"] * int(s))

def print_board(board):
  for row in board:
    print(" ".join(row))

def random_row(board):
  return randint(0, len(board) - 2)

def random_col(board):
  return randint(0, len(board[0]) - 2)

ship_row = random_row(board)
ship_col = random_col(board)
print("Lets Battleship!")
print_board(board)

# Important, will reccur. Used to generate a ship proportional to board.
print(*range(ship_row, (ship_row + int(s) // 5)))
print(*range(ship_col, (ship_col + int(s) // 5)))


for turn in range(int(int(s) / 5) + 2):
	    print("Turn", turn + 1, "Out of", int(s) - 5)   
	    guess_row = int(input("Guess Row:"))
	    guess_col = int(input("Guess Col:"))
	    if guess_row in range(ship_row, (ship_row + int(s) // 5)) and guess_col in range(ship_col, (ship_col + int(s) // 5)):
	        print("Congratulations! You hit my battleship!")
	        board[guess_row][guess_col] = "%"
# Debugging
	    elif guess_row == 000 and guess_col == 000:
	        break
	    elif guess_row == 111 and guess_col == 111:
	        board[ship_row][ship_col]  = "-"
	        board[ship_row + int(s) // 5][ship_col + int(s) // 5] = '-'
	    else:
	        if (guess_row < 0 or guess_row > len(board) - 1) or (guess_col < 0 or guess_col > len(board) - 1):
	            print("Oops, that's not even in the ocean.")
	        elif (board[guess_row][guess_col] == "X"):
	           print("You guessed that one already.")
	        else:
	            print("You missed my battleship!")
	            board[guess_row][guess_col] = "X"
	
	    print_board(board)
	
print("Game Over.")

		  

   
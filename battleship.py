from random import randint

def print_board(board):
	for row in range(0,len(board)):
		print "".join(board[row])
		
def random_coord(board):
	return randint(1,len(board))
	
def board_gen(board):
	for x in range(0,10):
		board.append(["O"]*10)
	return board
	
board=[]
board=board_gen(board)
print_board(board)

ship_row=random_coord(board)
ship_col=random_coord(board)

shot_row=random_coord(board)
shot_col=random_coord(board)

guess=0
tries=5
already_row=[]
already_col=[]

while guess < tries:
	valid_guess=0
	while valid_guess == 0:
		guess_row=input("Guess Row: ")
		guess_col=input("Guess Col: ")
		if guess_row in already_row:
			if guess_col in already_col:
				guess_row = 11
				print "You've already guessed that spot"
		already_row.append(guess_row)
		already_col.append(guess_col)
		if guess_row >=1 and guess_row < 11:
			if guess_col >=1 and guess_col < 11:
				valid_guess = 1
	if guess_row==ship_row and guess_col==ship_col:
		print "Congratulations! You sunk my battleship!"
		break
	else:
		print "MISS!"
		board[guess_row-1][guess_col-1]="X"
		print_board(board)
	guess+=1
print "Game Over"
if guess == tries:
	print "You Lose"
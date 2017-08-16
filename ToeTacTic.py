"""
Tic Tac Toe game - 2 players (no computer opponent)
 -wait for a player's input
 -validates the input, makes the move
 -output updated board
 -check win condition
"""
#Put imports here (if any are needed)


#CONSTANTS and Global variables here
w = 3
h = 3
p1 = "X"
p2 = "O"
#Declare board array of 1-9; still a 0 based array
board = [str(x+1) for x in range(w*h)]

#Define check_win() function to check if a player has won - returns T or F
def check_win():
	return False

#Define is_input_valid() function to check player's input - returns T or F
def is_input_valid(x):
	try:
		x = int(x)
	except:
		print("NOT A NUMBER")
		return False
	if 0<x<=w*h:
		if board[x-1] != p1 and board[x-1] != p2:
			return True
		print("UNAVAILABLE POSITION")
	else:
		print("OUTSIDE BOUNDS")
	return False

#Define player_input() function to receive a player's move
def player_input(turn):
	valid = False
	while(not valid):
		print("Player %s's turn. Enter position:" % turn)
		i_x = input("Position: ")
		if i_x == 'q':
			exit()
		valid = is_input_valid(i_x)
	#make move on the board
	board[int(i_x)-1] = turn
	#change turn
	if turn == p1:
		return p2
	else:
		return p1


#Define print_board() function to print the board to the terminal
def print_board():
	for index,p in enumerate(board):
		if (index+1) % 3 == 0 and index>0:
			print(p)
			if index<8:
				print("---------")
		else:
			print(p + " | ", end="")
	print()
	

#Define game_over() function to output the winner and end the game
def game_over():
	return

#Define main() function that will start the game and handle the main loop
def main():
	turn = p1
	print("Welcome to a game of Tic Tac Toe, 'q' to quit")
	print_board()
	while(not check_win()):
		turn = player_input(turn)
		print_board()
#call main()
main()
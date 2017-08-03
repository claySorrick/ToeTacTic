"""
Tic Tac Toe game - 2 players (no computer opponent)
 -wait for a player's input
 -validates the input, makes the move
 -output updated board
 -check win condition
"""
#Put imports here (if any are needed)


#CONSTANTS and Global variables here

#width and height of board
w = 3
h = 3

#creating an empty board array
board = [[' ' for x in range(w)] for y in range(h)]

#Define check_win() function to check if a player has won - returns T or F
def check_win():
	return False

#Define is_input_valid() function to check player's input - returns T or F
def is_input_valid(x,y):
	return True

#Define player_input() function to receive a player's move
def player_input():


#Define print_board() function to print the board to the terminal
def print_board():
	for row in board:
		for c in row[0:len(row)-1]:
			print(c + " | ", end="")
		print(row[len(row)-1])
	

#Define game_over() function to output the winner and end the game
def game_over():
	return

#Define main() function that will start the game and handle the main loop
def main():
	print("Welcome to a game of Tic Tac Toe, 'q' to quit")
	print_board()


#call main()
main()
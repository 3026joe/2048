import tkinter as tk
import sys
import random
import copy

board = []
next_board = []
prev_board = []
size = 4
highest = 2048
score = 0

def up(s, board):
	global score
	for c in range(s):
		for j in range(s):
			for i in range(s-1):
				if(board[i][j] == 0):
					board[i][j] = board[i+1][j]
					board[i+1][j] = 0
	for i in range(1, s):
		for j in range(s):
			if(board[i][j] != 0 and board[i][j] == board[i-1][j]):
				board[i-1][j] = board[i-1][j]*2
				score += board[i-1][j]
				board[i][j] = 0
	for c in range(s):
		for j in range(s):
			for i in range(s-1):
				if(board[i][j] == 0):
					board[i][j] = board[i+1][j]
					board[i+1][j] = 0
	return board

def down(s, board):
	global score
	for c in range(s):
		for j in range(s):
			i = s-1
			while(i >= 1):
				if(board[i][j] == 0):
					board[i][j] = board[i-1][j]
					board[i-1][j] = 0
				i -= 1
	i = s-2
	while(i >= 0):
		for j in range(s):
			if(board[i][j] != 0 and board[i][j] == board[i+1][j]):
				board[i+1][j] = board[i+1][j]*2
				score += board[i+1][j]
				board[i][j] = 0
		i -= 1
	for c in range(s):
		for j in range(s):
			i = s-1
			while(i >= 1):
				if(board[i][j] == 0):
					board[i][j] = board[i-1][j]
					board[i-1][j] = 0
				i -= 1
	return board

def left(s, board):
	global score
	for c in range(s):
		for i in range(s):
			for j in range(s-1):
				if(board[i][j] == 0):
					board[i][j] = board[i][j+1]
					board[i][j+1] = 0
	for j in range(1, s):
		for i in range(s):
			if(board[i][j] != 0 and board[i][j] == board[i][j-1]):
				board[i][j-1] = board[i][j-1]*2
				score += board[i][j-1]
				board[i][j] = 0
	for c in range(s):
		for i in range(s):
			for j in range(s-1):
				if(board[i][j] == 0):
					board[i][j] = board[i][j+1]
					board[i][j+1] = 0
	return board

def right(s, board):
	global score
	for c in range(s):
		for i in range(s):
			j = s-1
			while(j >= 1):
				if(board[i][j] == 0):
					board[i][j] = board[i][j-1]
					board[i][j-1] = 0
				j -= 1
	j = s-2
	while(j >= 0):
		for i in range(s):
			if(board[i][j] != 0 and board[i][j] == board[i][j+1]):
				board[i][j+1] = board[i][j+1]*2
				score += board[i][j+1]
				board[i][j] = 0
		j -= 1
	for c in range(s):
		for i in range(s):
			j = s-1
			while(j >= 1):
				if(board[i][j] == 0):
					board[i][j] = board[i][j-1]
					board[i][j-1] = 0
				j -= 1
	return board

def check(s, board):
	for i in range(s):
		for j in range(1, s):
			if(board[i][j] == board[i][j-1]):
				return 1
	for i in range(1, s):
		for j in range(s):
			if(board[i][j] == board[i-1][j]):
				return 1
	for i in board:
		if(0 in i):
			return 1
	return 0

def spawn(s, board):
	pos = []
	for i in range(s):
		for j in range(s):
			if(board[i][j] == 0):
				pos.append((i,j))
	p = random.choice(pos)
	n = random.randint(1,101)
	if(n >= 1 and n <= 90):
		board[p[0]][p[1]] = 2
	else:
		board[p[0]][p[1]] = 4
	return board

def check_new_high(s, board, high):
	for i in range(s):
		for j in range(s):
			if(board[i][j] == high):
				return 1
	return 0

def update_board(gui_obj, key):
	global board
	global next_board
	global highest
	global prev_board
	is_undo = 0
	if(key == "Up"):
		next_board = up(size, next_board)
	elif(key == "Down"):
		next_board = down(size, next_board)
	elif(key == "Left"):
		next_board = left(size, next_board)
	elif(key == "Right"):
		next_board = right(size, next_board)
	elif(key == "u"):
		is_undo = 1
		next_board = copy.deepcopy(prev_board)
	else:
		print("SOMETHING'S WRONG")
		exit(0)
	if(next_board == board):
		return
	if(not(is_undo)):
		prev_board = copy.deepcopy(board)
		next_board = spawn(size, next_board)
	board = copy.deepcopy(next_board)
	if(check(size, board) == 0):
		#add game over display
		print("GAME OVER")
		exit(0)
	if(check_new_high(size, board, highest)):
		#add new high tile display
		print("new highest reached ", highest)
		highest *= 2

class gui():
	def __init__(self):
		#colours
		global score
		self.top_frame_colour = "#faf8ef"
		self.board_frame_colour = "#bbada0"
		self.foreground_colours = {0: "#d6cdc4", 2:"#464646", 4:"#464646", 8:"#ffffff", 16:"#ffffff", 32:"#ffffff", 64:"#ffffff", 128:"#ffffff", 256:"#ffffff", 512:"#ffffff", 1024:"#ffffff", 2048:"#ffffff", 4096:"#ffffff", 8192:"#ffffff", 16384:"#ffffff", 32768:"#ffffff", 65536:"#ffffff", 131072:"#ffffff"}
		self.background_colours = {0: "#d6cdc4", 2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", 32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", 512:"#edc850", 1024:"#edc53f", 2048:"#edc22e", 4096:"#464646", 8192:"#3d3d3d", 16384:"#19191a", 32768:"#111111", 65536:"#09090a", 131072:"#000000"}
		self.board_font = ("Courier", 20, "bold")
		self.game_font = ("Courier", 30, "bold")
		self.home_game_font = ("Courier", 40, "bold")
		self.score_font = ("Promesh", 15, "bold")
		self.window = tk.Tk()
		self.homepage()

	def homepage(self):
		self.homepage_widgets = []
		background_frame = tk.Frame(master = self.window, bg = self.top_frame_colour, width = 435, height = 580)
		background_frame.pack()
		game_label = tk.Label(master = background_frame, text = "2048", font = self.home_game_font, fg = self.board_frame_colour, bg = self.top_frame_colour, width = 10, height = 2)
		game_label.pack()
		new_game_button = tk.Button(master = background_frame, text = "New Game", width = 10, height = 3, bg = self.board_frame_colour, fg = "#ffffff", command = self.home_start_game)
		new_game_button.pack()
		exit_button = tk.Button(master = background_frame, text = "Exit", width = 10, height = 3, bg = self.board_frame_colour, fg = "#ffffff", command = self.close_window)
		exit_button.pack()
		self.homepage_widgets.append(background_frame)
		self.homepage_widgets.append(game_label)
		self.homepage_widgets.append(new_game_button)
		self.homepage_widgets.append(exit_button)
		self.window.mainloop()

	def home_start_game(self):
		for i in self.homepage_widgets:
			i.destroy()
		self.start_game()

	def end_start_game(self):
		for i in self.widgets:
			for j in i:
				j[0].destroy()
				j[1].destroy()

		self.top_frame.destroy()
		self.game_label.destroy()
		self.new_game_button.destroy()
		self.exit_button.destroy()
		self.score_label.destroy()
		self.board_frame.destroy()
		self.start_game()

	def start_game(self):
		init_board()
		self.widgets = []
		self.top_frame = tk.Frame(master = self.window, bg = self.top_frame_colour)
		self.top_frame.pack(fill = tk.BOTH, expand = True)
		self.game_label = tk.Label(master = self.top_frame, text = "2048", font = self.game_font, fg = self.board_frame_colour, bg = self.top_frame_colour, width = 6, height = 3)
		self.game_label.grid(row = 0, column = 0, padx = 3, pady = 3)

		self.new_game_button = tk.Button(master = self.top_frame, text = "New Game", width = 9, height = 4, bg = self.board_frame_colour, fg = "#ffffff", command = self.end_start_game)
		self.new_game_button.grid(row = 0, column = 1, padx = 3, pady = 3)
		self.exit_button = tk.Button(master = self.top_frame, text = "Exit", width = 8, height = 4, bg = self.board_frame_colour, fg = "#ffffff", command = self.close_window)
		self.exit_button.grid(row = 0, column = 2, padx = 3, pady = 3)

		self.score_label = tk.Label(master = self.top_frame, text = "Score\n" + str(score), font = self.score_font, fg = "#ffffff", bg = self.board_frame_colour, width = 10, height = 3)
		self.score_label.grid(row = 0, column = 3, padx = 3, pady = 3)
		self.board_frame = tk.Frame(master = self.window, bg = self.board_frame_colour)
		self.board_frame.pack(fill = tk.BOTH, expand = True)
		self.create_board_gui()
		self.window.bind("<Up>", self.key_press)
		self.window.bind("<Down>", self.key_press)
		self.window.bind("<Right>", self.key_press)
		self.window.bind("<Left>", self.key_press)
		self.window.bind("<Key>", self.key_press)

	def close_window(self):
		exit(0)

	def create_board_gui(self):
		for i in range(size):
			self.widgets.append([])
			for j in range(size):
				frame = tk.Frame(master = self.board_frame, borderwidth = 1, relief = tk.RAISED)
				frame.grid(row = i, column = j, padx = 3, pady = 3)
				label = tk.Label(master = frame, text = str(board[i][j]), font = self.board_font, fg = self.foreground_colours[board[i][j]], bg = self.background_colours[board[i][j]], width = 6, height = 3)
				label.pack(fill = tk.BOTH, expand = True)
				self.widgets[i].append((frame, label))

	def key_press(self, event):
		key = event.keysym
		update_board(self, key)
		self.update_board_gui()

	def update_board_gui(self):
		global board
		global next_board
		global score
		self.score_label.config(text = "Score\n" + str(score))
		for i in range(size):
			for j in range(size):
				self.widgets[i][j][1].config(text = str(board[i][j]), fg = self.foreground_colours[board[i][j]], bg = self.background_colours[board[i][j]])

def init_board():
	global board
	global next_board
	global prev_board
	board = []
	for i in range(size):
		board.append([])
		for j in range(size):
			board[i].append(0)
	spawn(size, board)
	spawn(size, board)
	next_board = copy.deepcopy(board)
	prev_board = copy.deepcopy(board)

def main():
	print("initialization done")
	gui_obj = gui()

if __name__ == "__main__":
	main()
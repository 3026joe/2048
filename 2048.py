import tkinter as tk
import sys
import random
import copy

#colours
board_frame_colour = "#bbada0"
foreground_colours = {0: "#d6cdc4", 2:"#464646", 4:"#464646", 8:"#ffffff", 16:"#ffffff", 32:"#ffffff", 64:"#ffffff", 128:"#ffffff", 256:"#ffffff", 512:"#ffffff", 1024:"#ffffff", 2048:"#ffffff", 4096:"#ffffff", 8192:"#ffffff", 16384:"#ffffff", 32768:"#ffffff", 65536:"#ffffff", 131072:"#ffffff"}
background_colours = {0: "#d6cdc4", 2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", 32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", 512:"#edc850", 1024:"#edc53f", 2048:"#edc22e", 4096:"#464646", 8192:"#3d3d3d", 16384:"#19191a", 32768:"#111111", 65536:"#09090a", 131072:"#000000"}
board_font = ("Courier", 20, "bold")

def up(s, board):
	for c in range(s):
		for j in range(s):
			for i in range(s-1):
				if(board[i][j] == 0):
					board[i][j] = board[i+1][j]
					board[i+1][j] = 0
	for i in range(1, s):
		for j in range(s):
			if(board[i][j] == board[i-1][j]):
				board[i-1][j] = board[i-1][j]*2
				board[i][j] = 0
	for c in range(s):
		for j in range(s):
			for i in range(s-1):
				if(board[i][j] == 0):
					board[i][j] = board[i+1][j]
					board[i+1][j] = 0
	return board

def down(s, board):
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
			if(board[i][j] == board[i+1][j]):
				board[i+1][j] = board[i+1][j]*2
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
	for c in range(s):
		for i in range(s):
			for j in range(s-1):
				if(board[i][j] == 0):
					board[i][j] = board[i][j+1]
					board[i][j+1] = 0
	for j in range(1, s):
		for i in range(s):
			if(board[i][j] == board[i][j-1]):
				board[i][j-1] = board[i][j-1]*2
				board[i][j] = 0
	for c in range(s):
		for i in range(s):
			for j in range(s-1):
				if(board[i][j] == 0):
					board[i][j] = board[i][j+1]
					board[i][j+1] = 0
	return board

def right(s, board):
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
			if(board[i][j] == board[i][j+1]):
				board[i][j+1] = board[i][j+1]*2
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
	pos=[]
	for i in range(s):
		for j in range(s):
			if(board[i][j]==0):
				pos.append((i,j))
	p=random.choice(pos)
	n=random.randint(1,101)
	if(n>=1 and n<=90):
		board[p[0]][p[1]]=2
	else:
		board[p[0]][p[1]]=4
	return board

def check_new_high(s, board, high):
	for i in range(s):
		for j in range(s):
			if(board[i][j] == high):
				return 1
	return 0

class make_gui():
	def __init__(self, board):
		self.board = board
		self.board_copy = copy.deepcopy(board)
		# print(self.board_copy)
		# print(self.board)
		print("initialization done")
		self.window = tk.Tk()
		self.size = len(board)
		self.widgets = []
		self.highest = 2048
		self.board_frame = tk.Frame(master = self.window, bg = board_frame_colour)
		self.board_frame.pack(fill = tk.BOTH, expand = True)
		self.create_board_gui()
		self.window.bind("<Up>", self.update_board_gui)
		self.window.bind("<Down>", self.update_board_gui)
		self.window.bind("<Right>", self.update_board_gui)
		self.window.bind("<Left>", self.update_board_gui)
		self.window.mainloop()

	def create_board_gui(self):
		for i in range(self.size):
			self.widgets.append([])
			for j in range(self.size):
				frame = tk.Frame(master = self.board_frame, borderwidth = 1, relief = tk.RAISED)
				frame.grid(row = i, column = j, padx = 3, pady = 3)
				label = tk.Label(master = frame, text = str(self.board[i][j]), font = board_font, fg = foreground_colours[self.board[i][j]], bg = background_colours[self.board[i][j]], width = 6, height = 3)
				label.pack(fill = tk.BOTH, expand = True)
				self.widgets[i].append((frame, label))

	def update_board_gui(self, event):
		# print(self.board_copy)
		# print(self.board)
		if(event.keysym == "Up"):
			self.board_copy = up(self.size, self.board_copy)
		elif(event.keysym == "Down"):
			self.board_copy = down(self.size, self.board_copy)
		elif(event.keysym == "Left"):
			self.board_copy = left(self.size, self.board_copy)
		elif(event.keysym == "Right"):
			self.board_copy = right(self.size, self.board_copy)
		else:
			# print("SOMETHING'S WRONG")
			exit(0)
		if(self.board_copy == self.board):
			return
		self.board_copy = spawn(self.size, self.board_copy)
		self.board = copy.deepcopy(self.board_copy)
		# print(self.board_copy)
		# print(self.board)
		if(check(self.size, self.board) == 0):
			#add game over display
			print("GAME OVER")
			exit(0)
		if(check_new_high(self.size, self.board, self.highest)):
			#add new high tile display
			print("new highest reached ", self.highest)
			self.highest *= 2
		for i in range(self.size):
			for j in range(self.size):
				self.widgets[0][0][0].destroy()
				self.widgets[0][0][1].destroy()
				self.widgets[0].pop(0)
			self.widgets.pop(0)
		self.create_board_gui()



size=4
board=[]
for i in range(size):
	board.append([])
	for j in range(size):
		board[i].append(0)

spawn(size,board)
spawn(size,board)


gui = make_gui(board)
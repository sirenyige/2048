"""This file contains the 2048 Board class and performs all move operations"""

import random

class Board2048:
	def __init__(self):
		"""Begins the game, placing two new tiles on the board"""
		self.board = [[0, 0, 0, 0], 
					  [0, 0, 0, 0], 
					  [0, 0, 0, 0], 
					  [0, 0, 0, 0]]
		self.generate_new_tile()
		self.generate_new_tile()
		self.display_board()

	def generate_new_tile(self):
		"""Places a new tile on an empty square at random (2 with probability 0.9 and 2 with probability 0.9)"""
		# First, we find the empty squares
		empty_squares = []
		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				if self.board[i][j] == 0:
					empty_squares.append((i, j))

		# Next, select an empty square at random
		new_loc = empty_squares[random.randint(0, len(empty_squares) - 1)]

		# Select the value to place at that square
		if random.randint(1, 10) == 1:
			self.board[new_loc[0]][new_loc[1]] = 4
		else:
			self.board[new_loc[0]][new_loc[1]] = 2

	def swipe_left(self):
		"""Performs a left-swipe of the board"""
		marked_squares, initial_board = [], [row[:] for row in self.board]
		for y in range(1, len(self.board[0])):
			for x in range(len(self.board)):
				if self.board[x][y] != 0:
					i, j = x, y - 1
					while j >= 0 and self.board[i][j] == 0: 
						j = j - 1 # Identify how far left you can go
					if j >= 0 and self.board[x][y] == self.board[i][j] and (i, j) not in marked_squares:
						marked_squares.append((i, j))
						self.board[i][j], self.board[x][y] = 2*self.board[i][j], 0 # Perform merge and update
					else:
						j = j + 1
						if not (i == x and y == j):
							self.board[i][j], self.board[x][y] = self.board[x][y], 0 # Perform vanilla update

		# Check if swipe is valid
		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				if initial_board[i][j] != self.board[i][j]:
					self.generate_new_tile()
					self.display_board()
					return 0
		return -1

	def swipe_right(self):
		"""Performs a right-swipe of the board"""
		marked_squares, initial_board = [], [row[:] for row in self.board]
		for y in range(len(self.board[0]) - 2, -1, -1):
			for x in range(len(self.board)):
				if self.board[x][y] != 0:
					i, j = x, y + 1
					while j < len(self.board[0]) and self.board[i][j] == 0: 
						j = j + 1 # Identify how far left you can go
					if j < len(self.board[0]) and self.board[x][y] == self.board[i][j] and (i, j) not in marked_squares:
						marked_squares.append((i, j))
						self.board[i][j], self.board[x][y] = 2*self.board[i][j], 0 # Perform merge and update
					else:
						j = j - 1
						if not (i == x and y == j):
							self.board[i][j], self.board[x][y] = self.board[x][y], 0 # Perform vanilla update

		# Check if swipe is valid
		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				if initial_board[i][j] != self.board[i][j]:
					self.generate_new_tile()
					self.display_board()
					return 0
		return -1


	def swipe_up(self):
		"""Performs an upward-swipe of the board"""
		marked_squares, initial_board = [], [row[:] for row in self.board]
		for x in range(1, len(self.board)):
			for y in range(len(self.board)):
				if self.board[x][y] != 0:
					i, j = x - 1, y
					while i >= 0 and self.board[i][j] == 0: 
						i = i - 1 # Identify how far left you can go
					if i >= 0 and self.board[x][y] == self.board[i][j] and (i, j) not in marked_squares:
						marked_squares.append((i, j))
						self.board[i][j], self.board[x][y] = 2*self.board[i][j], 0 # Perform merge and update
					else:
						i = i + 1
						if not (i == x and y == j):
							self.board[i][j], self.board[x][y] = self.board[x][y], 0 # Perform vanilla update

		# Check if swipe is valid
		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				if initial_board[i][j] != self.board[i][j]:
					self.generate_new_tile()
					self.display_board()
					return 0
		return -1


	def swipe_down(self):
		"""Performs a downward-swipe of the board"""
		marked_squares, initial_board = [], [row[:] for row in self.board]
		for x in range(len(self.board[0]) - 2, -1, -1):
			for y in range(len(self.board)):
				if self.board[x][y] != 0:
					i, j = x + 1, y
					while i < len(self.board[0]) and self.board[i][j] == 0: 
						i = i + 1 # Identify how far left you can go
					if i < len(self.board[0]) and self.board[x][y] == self.board[i][j] and (i, j) not in marked_squares:
						marked_squares.append((i, j))
						self.board[i][j], self.board[x][y] = 2*self.board[i][j], 0 # Perform merge and update
					else:
						i = i - 1
						if not (i == x and y == j):
							self.board[i][j], self.board[x][y] = self.board[x][y], 0 # Perform vanilla update

		# Check if swipe is valid
		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				if initial_board[i][j] != self.board[i][j]:
					self.generate_new_tile()
					self.display_board()
					return 0
		return -1


	def display_board(self):
		"""Displays a basic version of the 2048 gameboard"""
		col_width = len('2048')
		for i in range(len(self.board)):
			print(' '.join(str(val).ljust(col_width) for val in self.board[i]))
			print()

	def can_move(self):
		"""Determines whether any valid moves exist"""
		initial_board = [row[:] for row in self.board]
		if self.swipe_left() == -1 and self.swipe_right() == -1 and self.swipe_up() == -1 and self.swipe_down() == -1:
			return False
		else:
			self.board = initial_board
			return True

	def has_won(self):
		"""Determines if the current board configuration is a winning one"""
		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				if self.board[i][j] == 2048:
					return True
		return False

	def make_moves(self):
		"""Just does a bunch of moves"""
		while self.can_move() and not self.has_won():
			if self.swipe_left() != -1:
				continue
			elif self.swipe_up() != -1:
				continue
			elif self.swipe_right() != -1:
				continue
			self.swipe_down()

		if self.has_won():
			return 1
		return 0


"""This file contains the functions that implement the 2048-AI"""

import game_simulator
import random
import queue

class Player2048:

	def __init__(self, display=True):
		"""Initializes a 2048 Player that plays the game"""
		self.b = game_simulator.Board2048(display)

	def play_game(self, display=True):
		"""Uses decision tree to achieve highest possible 2048 score"""
		self.b.reset_board(display)
		for _ in range(random.randint(3, 10)):
			self.make_naive_move(display)

		count = 0
		while not self.b.has_won() and self.b.can_move():
			self.make_move(display)

		if self.b.has_won():
			return 1
		return 0

	def make_move(self, display=True):
		"""Selects and makes the optimal move"""
		move = self.evaluate()
		if move == 0:
			self.b.swipe_left(display)
		elif move == 1:
			self.b.swipe_up(display)
		elif move == 2:
			self.b.swipe_right(display)
		elif move == 3:
			self.b.swipe_down(display)
		elif move == -1:
			self.b.display_board()

	def make_naive_move(self, display=True):
		"""Starts the game by making a few naive moves"""
		x = random.randint(1, 10)
		if x <= 5:
			self.b.swipe_left(display)
		else:
			self.b.swipe_up(display)

	def evaluate(self):
		"""Evaluation function which assigns a numerical score to input position"""
		optimal_move, max_diff, curr_score = -1, -float("inf"), self.b.score

		for i in range(16):
			self.b.cache_board()
			if i%4 == 0:
				valid = self.b.swipe_left(False)
				if self.b.can_move() and (self.b.score - curr_score) > max_diff and valid != -1:
					optimal_move, max_diff = i, self.b.score - curr_score
			elif i%4 == 1:
				valid = self.b.swipe_up(False) 
				if self.b.can_move() and (self.b.score - curr_score) > max_diff and valid != -1:
					optimal_move, max_diff = i, self.b.score - curr_score
			elif i%4 == 2:
				valid = self.b.swipe_right(False)
				if self.b.can_move() and (self.b.score - curr_score) > max_diff and valid != -1:
					optimal_move, max_diff = i, self.b.score - curr_score
			elif i%4 == 3:
				valid = self.b.swipe_down(False)
				if self.b.can_move() and (self.b.score - curr_score) > max_diff and valid != -1:
					optimal_move, max_diff = i, self.b.score - curr_score
			self.b.board = self.b.cached_board
			self.b.score = self.b.cached_score
		return optimal_move


	def compute_divisor(self, board):
		max_tile, second_max_tile, third_max_tile = 0, 0, 0
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] > max_tile:
					max_tile, second_max_tile, third_max_tile = board[i][j], max_tile, second_max_tile
				elif board[i][j] > second_max_tile:
					second_max_tile, third_max_tile = board[i][j], second_max_tile
				elif board[i][j] > third_max_tile:
					third_max_tile = board[i][j]

		if board[0][0] != max_tile and board[0][1] != second_max_tile and board[0][2] != third_max_tile:
			return 2048
		elif board[0][0] != max_tile and board[0][1] != second_max_tile:
			return 1024
		elif board[0][0] != max_tile and board[0][2] != third_max_tile:
			return 512
		elif board[0][1] != second_max_tile and board[0][2] != third_max_tile:
			return 256
		elif board[0][0] != max_tile:
			return 512
		elif board[0][1] != second_max_tile:
			return 256
		elif board[0][2] != third_max_tile:
			return 32
		return 1

	def play_many_games(self):
		while True:
			has_won = self.play_game(False)
			if has_won:
				print("Largest tile:", 2048)
				break
			else:
				largest_tile = 0
				for i in range(len(self.b.board)):
					for j in range(len(self.b.board[0])):
						if largest_tile < self.b.board[i][j]:
							largest_tile = self.b.board[i][j]
				print("Largest tile:", largest_tile)
				self.b.reset_board(False)


######################
# UNDER CONSTRUCTION #
######################

class PositionTree:
	def __init__(self, node):
		"""Initializes a PositionTree object"""
		self.root = node

class Node:
	def __init__(self, board, score, label=-1):
		"""Initializes a PositionTree Node"""
		self.board = board
		self.score = score
		self.label = label
		self.branches = []

	def add_branch(self, node):
		self.branches.append(node)
		
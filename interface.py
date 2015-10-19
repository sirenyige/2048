import tkinter as tk
import game_simulator as sim 

# Constants
square_dim = 100
canvas_width = 400
canvas_height = 400
color_map = {   0 : "#d3d3d3",
				2 : "#eee4da",
			    4 : "#ede0c8",
			    8 : "#f2b179",
			   16 : "#f59563",
			   32 : "#f67c5f",
			   64 : "#f65e3b",
			  128 : "#edcf72",
			  256 : "#edcc61",
			  512 : "#edc850",
			 1024 : "#edc53f",
			 2048 : "#edc22e"
			}

size_map = {    2 : 60,
			    4 : 60,
			    8 : 60,
			   16 : 48,
			   32 : 48,
			   64 : 48,
			  128 : 36,
			  256 : 36,
			  512 : 36,
			 1024 : 24,
			 2048 : 24
		   }

offset_map = {    2 : 35,
			      4 : 35,
			      8 : 35,
			     16 : 25,
			     32 : 25,
			     64 : 25,
			    128 : 20,
			    256 : 20,
			    512 : 20,
			   1024 : 5,
			   2048 : 5
		     }

# Initializations
root = tk.Tk()
root.title("2048")

b = sim.Board2048()

canvas = tk.Canvas(root, width=canvas_width,height=canvas_height)
canvas.pack()

def generate_board():
	"""Generates the current board configuration"""
	for i in range(len(b.board)):
		for j in range(len(b.board[0])):
			num = b.board[i][j]
			background_color = color_map[num]
			if num != 0:
				print(i, j)
			canvas.create_rectangle(j*100, i*100, (j+1)*100, (i+1)*100, fill=background_color)
			if num != 0:
				if num == 2 or num == 4:
					num_color = "#776e65"
				else:
					num_color = "#f9f6f2"
				canvas.create_text(j*100 + offset_map[num], i*100 + 50, anchor=tk.W, font=("Arial", size_map[num]), text=str(num), fill=num_color)

def check_key_pressed(event):
	"""Checks if a swipe has been performed, and updates the board appropriately"""
	if event.keysym == 'Left':
		b.swipe_left()
	elif event.keysym == 'Right':
		b.swipe_right()
	elif event.keysym == 'Up':
		b.swipe_up()
	elif event.keysym == 'Down':
		b.swipe_down()
	generate_board()
	root.after(100, check_key_pressed)

# Set up and loop
button = tk.Button(root, text='New Game', width=25, command=b.reset_board)
generate_board()
button.pack()
root.bind_all('<KeyPress>', check_key_pressed)
root.after(100, check_key_pressed)
root.mainloop()
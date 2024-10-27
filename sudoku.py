import tkinter as tk
import numpy as np
from tkinter import messagebox


# Initial Board with prefilled values
initial_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def is_valid_move(board, row, col, num):
    # Check row and column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


class Sudoku:

    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.cells = {}

        self.create_board()

        check_button = tk.Button(self.root, text="Check Solutions", command=self.check_solution)
        check_button.grid(row=10, column=10, columnspan=9)

    def create_board(self):
        for row in range(9):
            for col in range(9):
                cell_value = initial_board[row][col]
                entry = tk.Entry(self.root, width=3, font=("Arial", 18), justify="center")

                if cell_value != 0:
                    entry.insert(0, str(cell_value))
                    entry.config(state="disabled")
                else:
                    entry.bind("<FocusOut>", self.update_board)
                
                entry.grid(row=row, column=col, padx=5, pady=5)
                self.cells[(row, col)] = entry

    def update_board(self, event):
        for (row, col), entry in self.cells.items():
            if entry.get().isdigit():
                initial_board[row][col] = int(entry.get())
            else:
                initial_board[row][col] = 0
    
    def check_solution(self):
        for row in range(9):
            for col in range(9):
                num = initial_board[row][col]
                if num == 0 or not is_valid_move(initial_board, row, col, num):
                    messagebox.showinfo("Sudoku", "The solution is incorrect.")
                    return
        
        messagebox.showinfo("Sudoku", "Congratulations! You solved the puzzle correctly.")


root = tk.Tk()
game = Sudoku(root)
root.mainloop()
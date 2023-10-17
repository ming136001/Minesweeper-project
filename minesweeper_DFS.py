#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import random

class Minesweeper:
    def __init__(self, root, rows, cols, num_mines):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.game_over = False
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        self.create_mines()
        self.create_gui()

    def create_mines(self):
        mines = random.sample(range(self.rows * self.cols), self.num_mines)
        for mine in mines:
            row = mine // self.cols
            col = mine % self.cols
            self.board[row][col] = -1

    def create_gui(self):
        for i in range(self.rows):
            for j in range(self.cols):
                button = tk.Button(self.root, text=" ", width=2, height=2, command=lambda i=i, j=j: self.click(i, j))
                button.grid(row=i, column=j)
                
                # Set the background color to white and font size to a larger value
                button.config(bg='black', font=("Helvetica", 37))  # Change the font size as needed

                self.buttons[i][j] = button

    def click(self, row, col):
        if self.game_over:
            return

        if self.board[row][col] == -1:
            self.reveal_mines()
            self.game_over = True
            for i in range(self.rows):
                for j in range(self.cols):
                    self.buttons[i][j].config(bg='green')  # Change to green
            return

        count = self.count_mines_around(row, col)
        if count == 0:
            self.dfs_reveal(row, col)
            self.buttons[row][col].config(text="0")
            self.buttons[row][col].config(state=tk.DISABLED)
        else:
            self.buttons[row][col].config(text=str(count))
            self.buttons[row][col].config(state=tk.DISABLED)

    def count_mines_around(self, row, col):
        count = 0
        for direction in self.directions:
            dr, dc = direction[0] + row, direction[1] + col

            if (0 <= dr < self.rows) and (0 <= dc < self.cols) and (self.board[dr][dc] == -1):
                count += 1
        return count

    def dfs_reveal(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            for direction in self.directions:
                dr, dc = direction[0] + row, direction[1] + col
                if 0 <= dr < self.rows and 0 <= dc < self.cols and self.buttons[dr][dc]['state'] != tk.DISABLED:
                    result = self.count_mines_around(dr, dc)
                    self.buttons[dr][dc].config(text=str(result))
                    self.buttons[dr][dc].config(state=tk.DISABLED)
                    if result == 0:
                        self.dfs_reveal(dr, dc)

    def reveal_mines(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == -1:
                    self.buttons[i][j].config(text="X")

def main():
    root = tk.Tk()
    root.title("Minesweeper")
    rows, cols, num_mines = 14, 14, 20
    game = Minesweeper(root, rows, cols, num_mines)
    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:





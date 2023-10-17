# Minesweeper-project(python)
## Project Description
-Minesweeper is a Minesweeper is a classic single-player puzzle game . In Minesweeper, the player is presented with a grid of cells, 
some of which contain hidden mines, while others are empty. The objective of the game is to uncover all the empty cells without triggering any 
mines. The game is both fun and a great exercise in logical deduction and problem-solving.
## Data Structure and Algorithm used:
- 2D Array 
- Depth First Search Algorithm
## Depth first search in reveal function
```Python
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
```
- If a cell has no mine next to it,then we use a DFS algorithm to explore the cells next to it to expand the area until it reaches a boundary that is adjacent to any mine. 


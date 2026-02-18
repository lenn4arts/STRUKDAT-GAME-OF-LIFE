import time
import os
import random

# Ukuran grid
ROWS = 20
COLS = 40

def create_grid():
    return [[random.randint(0, 1) for _ in range(COLS)] for _ in range(ROWS)]

def print_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print("".join("■" if cell else " " for cell in row))

def count_neighbors(grid, r, c):
    directions = [-1, 0, 1]
    count = 0
    for dr in directions:
        for dc in directions:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                count += grid[nr][nc]
    return count

def update_grid(grid):
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    
    for r in range(ROWS):
        for c in range(COLS):
            neighbors = count_neighbors(grid, r, c)
            
            if grid[r][c] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[r][c] = 0
                else:
                    new_grid[r][c] = 1
            else:
                if neighbors == 3:
                    new_grid[r][c] = 1
                    
    return new_grid

def main():
    grid = create_grid()
    
    while True:
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(0.2)

if __name__ == "__main__":
    main()

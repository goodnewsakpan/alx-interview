#!/usr/bin/python3
def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Start by adding 4 for each land cell
                perimeter += 4
                
                # Subtract for adjacent land cells
                if r > 0 and grid[r - 1][c] == 1:  # Check the cell above
                    perimeter -= 1
                if r < rows - 1 and grid[r + 1][c] == 1:  # Check the cell below
                    perimeter -= 1
                if c > 0 and grid[r][c - 1] == 1:  # Check the cell to the left
                    perimeter -= 1
                if c < cols - 1 and grid[r][c + 1] == 1:  # Check the cell to the right
                    perimeter -= 1

    return perimeter


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

                # Subtract 1 for adjacent land cells (above and left only)
                if r > 0 and grid[r - 1][c] == 1:  # Check the cell above
                    perimeter -= 2  # Shared edge between current cell and the cell above
                if c > 0 and grid[r][c - 1] == 1:  # Check the cell to the left
                    perimeter -= 2  # Shared edge between current cell and the cell to the left

    return perimeter

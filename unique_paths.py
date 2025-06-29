# Example exercise. Calculate the number of unique paths in a set of grids with obstacles.
# 1 = obstacle, 0 = free space
import time
GRIDS = [
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ],
    [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ],
    [
        [0, 1],
        [1, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
    ]
]

def unique_paths_recursive(grid, i=0, j=0):
    m, n = len(grid), len(grid[0])
    if i >= m or j >= n or grid[i][j] == 1:
        return 0
    if i == m - 1 and j == n - 1:
        return 1
    return unique_paths_recursive(grid, i + 1, j) + unique_paths_recursive(grid, i, j + 1)

if __name__ == "__main__":
    for idx, grid in enumerate(GRIDS):
        print(f"Grid {idx + 1}: {unique_paths_recursive(grid)} unique paths")

from aoc.utils.common import read_grid
import time

# 8-directional neighbor offsets
DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

def count_adjacent_rolls(grid, i, j):
    n = len(grid)
    m = len(grid[0])
    cnt = 0
    for di, dj in DIRS:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == "@":
            cnt += 1
    return cnt

def solve():
    grid = read_grid()
    n = len(grid)
    m = len(grid[0])

    total_removed = 0

    while True:
        to_remove = []

        # Phase 1: find all rolls that are accessible in the *current* grid
        for i in range(n):
            for j in range(m):
                if grid[i][j] != "@":
                    continue
                neighbors = count_adjacent_rolls(grid, i, j)
                if neighbors < 4:
                    to_remove.append((i, j))

        # If nothing can be removed in this pass, we're done
        if not to_remove:
            break

        # Phase 2: remove all found rolls at once
        for i, j in to_remove:
            grid[i][j] = "."

        total_removed += len(to_remove)

    print(f"Forklift can access {total_removed} rolls")

if __name__ == "__main__":
    start_time = time.perf_counter()
    solve()
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"\nFunction executed in {duration:.4f} seconds.")

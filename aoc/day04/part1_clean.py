from aoc.utils.common import read_grid
import time

DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

def solve():
    grid = read_grid()
    n = len(grid)
    m = len(grid[0])

    total = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] != "@":
                continue

            neighbors = 0

            for di, dj in DIRS:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] == "@":
                        neighbors += 1

            if neighbors < 4:
                total += 1

    print(f"Forklift can access {total} rolls")

if __name__ == "__main__":
    start_time = time.perf_counter()
    solve()
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"\nFunction executed in {duration:.4f} seconds.")

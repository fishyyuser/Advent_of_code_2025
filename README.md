# 🎄 Advent of Code 2025 — Python Solutions

Welcome to my **Advent of Code 2025** repository!  
This repository contains Python solutions for all 12 days of Advent of Code 2025.

Each solution prioritizes correctness and clear structure, with performance
considerations applied where required by the problem constraints.



## 🧩 Goals

- Provide correct and complete solutions for each Advent of Code problem
- Keep implementations readable and logically structured
- Use appropriate algorithms and data structures per problem requirements
- Maintain consistency across all solution files



## 📁 Repository Structure

```bash
Advent_of_code_2025/
├── aoc/
    ├── day01/
    │   ├── part1.py
    │   ├── part2.py
    │   └── input.txt
    ├── day02/
    ├── ...
    ├── day12/
    └── utils/
        ├── common.py
        └── __init__.py
```

Each day contains:

- `part1.py` — solution for Part 1
- `part2.py` — solution for Part 2
- `input.txt` — puzzle input
- (the input helpers live inside `aoc/utils/common.py`)



## 🚀 Running Solutions

From the **project root**, run any day using module execution:

```bash
python -m aoc.dayXX.part1
python -m aoc.dayXX.part2
```

All solutions use **Python 3.11.14**.



## 🛠️ Python Techniques

Depending on the day, solutions may involve:

- Graph traversal (DFS / BFS)
- Path counting with memoization
- Backtracking with pruning and ordering heuristics
- Flood fill and region expansion
- Bitmask / bitboard representations
- Constraint satisfaction and feasibility checks
- Greedy and problem-specific strategies
- Connected component construction and merging
- Grid and coordinate-based geometry
- Shape normalization via rotation and reflection

Later problems required careful state-space reduction and
performance-driven design to remain tractable.

## 📜 License

This project is licensed under the **MIT License**.

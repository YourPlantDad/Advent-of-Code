# 🌟 Advent of Code - YourPlantDad's solutions Repository 🎄
Welcome to my personal archive of solutions for the annual **Advent of Code (AoC)** programming challenges\!

This repository serves as a collection of my attempts and final solutions, primarily implemented in **Python**. It's designed to track progress, showcase problem-solving techniques, and celebrate the annual December tradition.

## Repository Structure
Solutions are organized into folders by the challenge year. Within each year, solutions are separated by the specific Day number.
```
Advent-of-Code/
├── 2025/
│   ├── Day_01/
│   │   ├── day_01.py       # Python solution script
│   │   └── input.txt     # The unique puzzle input
│   ├── Day_02/
│   │   └── ...
│   └── README.md         # (Optional: Year-specific notes)
└── README.md             # <- You are here
```

## Featured Solution: 2025 Day 01 - Secret Entrance
The first challenge introduced a classic "wraparound" problem involving a circular safe dial (0-99). The core difficulty lies in handling the boundary conditions efficiently.
### Key Concepts
1.  **Circular Arithmetic (Modulo):** The dial runs from 0 to 99, meaning there are $\mathbf{100}$ possible positions. All final position calculations must use the **modulo operator** (`% 100`) to ensure the result wraps correctly.
    * Example: $50 + R68 \Rightarrow 118 \pmod{100} = 18$
    * Example: $50 + L68 \Rightarrow 50 - 68 = -18$. Python handles negative modulo correctly: $-18 \pmod{100} = 82$.

2.  **Part One:** **End-of-Rotation Count**

    * Goal: Count how many times the `current_dial_position` is exactly **0** *after* a rotation is complete. This is a straightforward check after applying the modulo operation.

3.  **Part Two:** **Click Count** (Method 0x434C49434B)

      * Goal: Count every time the dial clicks past **0** *during* a rotation, including the final stopping point if it's 0.
      * **Implementation:** This is solved by using **integer division** ($\lfloor \cdot \rfloor$) to calculate how many times the movement crosses a multiple of 100 between the start and end positions, avoiding a slow click-by-click loop.

| Scenario | Start Pos | Move | Raw End | Zero Crossings (Clicks on 0) |
| :---: | :---: | :---: | :---: | :---: |
| Normal | 50 | R30 | 80 | 0 |
| Positive Wrap | 50 | R68 | 118 | 1 |
| Multiple Wraps | 50 | R260 | 310 | 3 |
| Negative Wrap | 10 | L20 | -10 | 1 |

The `day_01.py` solution includes the optimized calculation to determine these zero crossings based on the size and direction of the step.

## Getting Started

To run any solution:

1.  Navigate to the specific day's directory (e.g., `2025/Day_01`).
2.  Execute the Python script from your terminal:
    ```bash
    python day_01.py
    ```
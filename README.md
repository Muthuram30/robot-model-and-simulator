
# Robot Model and Simulator

## Overview

This project is a **Python-based robot simulator** that operates in a 2D grid world.
The robot can be placed inside a defined grid, move in different directions, rotate, and manage battery levels.

The simulator also supports **Undo and Redo functionality**, allowing users to revert or reapply previous actions.

---

## Features

* Grid-based world with configurable **width and height**
* Robot placement with position and orientation
* Movement based on orientation (**N, S, E, W**)
* Rotation (left or right)
* Battery consumption and charging
* Boundary checking to prevent leaving the grid
* **Undo and Redo system** to track state history
* Status reporting

---

## Robot State

The robot maintains the following state variables:

* **Position:** `(x, y)`
* **Orientation:** `N`, `S`, `E`, or `W`
* **Battery Level:** `0 – 100%`

Each valid command updates and stores the robot state in history.

---

## Available Commands

| Command | Description                    |
| ------- | ------------------------------ |
| 1       | Place the robot in the grid    |
| 2       | Move the robot forward         |
| 3       | Rotate the robot left or right |
| 4       | Charge the battery             |
| 5       | Show current robot status      |
| 6       | Undo last command              |
| 7       | Redo last command              |
| 0       | Exit the simulator             |

---

## How It Works

1. The user defines the **world dimensions**.
2. The robot must be **placed on the grid** before performing actions.
3. Movement consumes battery based on number of steps.
4. Boundary checks ensure the robot stays within the grid.
5. Every action is stored so that **Undo/Redo operations** can restore previous states.

---

## Example Workflow

```
1) Place robot
Enter x position: 10
Enter y position: 20
Enter orientation: N

2) Move robot
Enter number of steps: 5

3) Rotate robot
Enter rotation left(0) or right(1): 1

5) Report status
```

---

## Requirements

* Python 3.x


---


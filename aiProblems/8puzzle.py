import numpy as np
import json


def findEmptyTile(initial):
    for i in range(initial.shape[0]):
        for j in range(initial.shape[1]):
            if initial[i][j] == 0:
                return i, j
    return -1, -1


def moveUp(current, row, col):
    if (row - 1) >= 0:
        new_state = np.copy(current)
        new_state[row][col], new_state[row - 1][col] = new_state[row - 1][col], new_state[row][col]

        return new_state
    return None


def moveDown(current, row, col):
    if (row + 1) < current.shape[0]:
        new_state = np.copy(current)
        new_state[row][col], new_state[row + 1][col] = new_state[row + 1][col], new_state[row][col]

        return new_state
    return None


def moveRight(current, row, col):
    if (col + 1) < current.shape[1]:
        new_state = np.copy(current)
        new_state[row][col + 1], new_state[row][col] = new_state[row][col], new_state[row][col + 1]

        return new_state
    return None


def moveLeft(current, row, col):
    if (col - 1) >= 0:
        new_state = np.copy(current)
        new_state[row][col - 1], new_state[row][col] = new_state[row][col], new_state[row][col - 1]

        return new_state
    return None


def solveBFS(initial, goal):
    print("Solving 8 puzzle through BFS:")
    counter = 1
    # Initialising frontier
    frontier = [(initial,"")]
    explored = set()

    while frontier:
        # Acquire state from frontier
        current,path = frontier.pop(0)

        # Convert the current state to a string for hashing
        current_str = str(current)

        # Check if current state has been explored
        if current_str in explored:
            continue

        # Add current state to explored set
        explored.add(current_str)



        # Check if current state is the goal state
        if np.array_equal(current, goal):
            print("Solution found!!!")
            return counter,path
            break

        row, col = findEmptyTile(current)


        # Applying operators and storing children
        # Move up
        new_state = moveUp(current, row, col)
        if new_state is not None:
            frontier.append((new_state,path+"UP  "))

        # Move right
        new_state = moveRight(current, row, col)
        if new_state is not None:
            frontier.append((new_state,path+"Right  "))

        # Move down
        new_state = moveDown(current, row, col)
        if new_state is not None:
            frontier.append((new_state,path+"Down  "))

        # Move left
        new_state = moveLeft(current, row, col)
        if new_state is not None:
            frontier.append((new_state,path+"Left  "))

        counter += 1

    return counter


# Driver code
print("Welcome to 8 puzzle problem")
initial = np.array([
    [1, 0, 3],
    [4, 5, 7],
    [2, 8, 6]
], dtype='int16')

goal = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
])

steps,path = solveBFS(initial, goal)
print("Puzzle solved with ", steps, "Steps")
print("Path taken from initial state : ",path)


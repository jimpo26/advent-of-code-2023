with open('input.txt', 'r') as f:
    maze = f.readlines()
maze = [list(row.strip()) for row in maze]
visited = set()


def is_valid_move(maze, row, col, direction):
    if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and (row, col) not in visited:
        if direction == 'N':
            return maze[row + 1][col] in ['|', 'J', 'L', 'S'] and maze[row][col] in ['|', '7', 'F']
        elif direction == 'S':
            return maze[row - 1][col] in ['|', '7', 'F', 'S'] and maze[row][col] in ['|', 'J', 'L']
        elif direction == 'W':
            return maze[row][col + 1] in ['-', '7', 'J', 'S'] and maze[row][col] in ['-', 'F', 'L']
        elif direction == 'E':
            return maze[row][col - 1] in ['-', 'F', 'L', 'S'] and maze[row][col] in ['-', '7', 'J']
    return False


# find index of S in maze
def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                return i, j


p = find_start(maze)
if is_valid_move(maze, p[0] - 1, p[1], 'N'):
    if is_valid_move(maze, p[0], p[1] - 1, 'W'):
        maze[p[0]][p[1]] = 'J'
    elif is_valid_move(maze, p[0], p[1] + 1, 'E'):
        maze[p[0]][p[1]] = 'L'
elif is_valid_move(maze, p[0] + 1, p[1], 'S'):
    if is_valid_move(maze, p[0], p[1] - 1, 'W'):
        maze[p[0]][p[1]] = '7'
    elif is_valid_move(maze, p[0], p[1] + 1, 'E'):
        maze[p[0]][p[1]] = 'F'
elif is_valid_move(maze, p[0], p[1] - 1, 'W'):
    if is_valid_move(maze, p[0] - 1, p[1], 'N'):
        maze[p[0]][p[1]] = 'J'
    elif is_valid_move(maze, p[0] + 1, p[1], 'S'):
        maze[p[0]][p[1]] = '7'
elif is_valid_move(maze, p[0], p[1] + 1, 'E'):
    if is_valid_move(maze, p[0] - 1, p[1], 'N'):
        maze[p[0]][p[1]] = 'L'
    elif is_valid_move(maze, p[0] + 1, p[1], 'S'):
        maze[p[0]][p[1]] = 'F'


def start():
    current = (p[0], p[1])
    visited.add(current)
    while True:
        if is_valid_move(maze, current[0] - 1, current[1], 'N'):
            visited.add((current[0] - 1, current[1]))
            current = (current[0] - 1, current[1])
        elif is_valid_move(maze, current[0] + 1, current[1], 'S'):
            visited.add((current[0] + 1, current[1]))
            current = (current[0] + 1, current[1])
        elif is_valid_move(maze, current[0], current[1] - 1, 'W'):
            visited.add((current[0], current[1] - 1))
            current = (current[0], current[1] - 1)
        elif is_valid_move(maze, current[0], current[1] + 1, 'E'):
            visited.add((current[0], current[1] + 1))
            current = (current[0], current[1] + 1)
        else:
            break

    print(len(visited) // 2)
start()
frees = 0
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if (i,j) not in visited:  # not part of the loop
            # ray in polygon algorithm.
            edges = 0
            for k in range(j):
                if (i, k) not in visited:
                    continue
                edges += maze[i][k] in ['|', '7', 'F']
            if edges % 2 == 1:
                frees += 1



print(frees)

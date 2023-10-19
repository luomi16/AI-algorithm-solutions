# Import Libraries
from collections import deque
from heapq import heappop, heappush

# Pancake Flipping Function


def flip(s, i):
    flipped = ""
    for j in range(0, 2*i, 2):
        number = s[j]
        color = 'w' if s[j+1] == 'b' else 'b'
        flipped = number + color + flipped
    return flipped + s[2*i:]

# Heuristic Function


def heuristic(state):
    goal = ''.join([str(i) for i in range(1, len(state) // 2 + 1)])
    actual = ''.join([state[i] for i in range(0, len(state), 2)])
    return sum(1 for a, b in zip(goal, actual) if a != b)

# BFS Search Function


def bfs_pancake(start):
    goal = start.replace("b", "w")
    visited = set()
    queue = deque([(start, [])])

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        for i in range(1, len(start) // 2 + 1):
            new_state = flip(state, i)
            if new_state not in visited:
                visited.add(new_state)
                new_path = path + [state[:2*i] + "|" + state[2*i:]]
                queue.append((new_state, new_path))

    return []

# A* Search Function


def a_star_pancake(start):
    goal = start.replace("b", "w")
    visited = set()
    queue = [(heuristic(start), 0, start, [])]

    while queue:
        f, g, state, path = heappop(queue)

        if state == goal:
            return path + [(state, g, 0)]

        for i in range(1, len(start) // 2 + 1):
            new_state = flip(state, i)
            if new_state not in visited:
                visited.add(new_state)
                h = heuristic(new_state)
                new_g = g + i
                new_path = path + [(state[:2*i] + "|" + state[2*i:], g, f - g)]
                heappush(queue, (h + new_g, new_g, new_state, new_path))

    return []


start_input = input("Please input，for example：1b2b3w4b-X：")
start, search_type = start_input[:-2], start_input[-1]

if search_type == "b":
    steps = bfs_pancake(start)
    print("Steps (BFS):")
    for step in steps:
        print(step)
elif search_type == "a":
    steps = a_star_pancake(start)
    print("Steps (A*):")
    for step, g, h in steps:
        print(f"{step} g:{g}, h:{h}")
else:
    print("Invalid Input!")

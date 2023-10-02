from heapq import heappop, heappush


def flip(s, i):
    flipped = ""
    for j in range(0, 2*i, 2):
        number = s[j]
        color = 'w' if s[j+1] == 'b' else 'b'
        flipped = number + color + flipped
    return flipped + s[2*i:]


def heuristic(state):
    goal = ''.join([str(i) for i in range(1, len(state) // 2 + 1)])
    actual = ''.join([state[i] for i in range(0, len(state), 2)])
    return sum(1 for a, b in zip(goal, actual) if a != b)


def a_star_pancake(start):
    goal = start.replace("b", "w")
    visited = set()
    queue = [(heuristic(start), 0, start, [])]  # (f, g, state, path)

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
                new_path = path + \
                    [(state[:2*i] + "|" + state[2*i:], g, f - g)]
                heappush(queue, (h + new_g, new_g, new_state, new_path))

    return []


start = "1w2w3b4w"
steps = a_star_pancake(start)
print("Steps:")
for step, g, h in steps:
    print(f"{step} g:{g}, h:{h}")

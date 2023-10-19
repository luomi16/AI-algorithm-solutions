from collections import deque


def flip(s, i):
    # 翻转前i个煎饼，保持每个煎饼的数字和字母顺序
    flipped = ""
    for j in range(0, 2*i, 2):
        number = s[j]
        color = 'w' if s[j+1] == 'b' else 'b'
        flipped = number + color + flipped
    return flipped + s[2*i:]


def bfs_pancake(start):
    goal = start.replace("b", "w")
    visited = set()
    queue = deque([(start, [])])  # (状态, 操作列表)

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        for i in range(1, len(start) // 2 + 1):
            new_state = flip(state, i)
            if new_state not in visited:
                visited.add(new_state)
                # 将当前状态和翻转位置添加到操作列表中
                new_path = path + [state[:2*i] + "|" + state[2*i:]]
                queue.append((new_state, new_path))

    return []


start = "1w2b3b4w"
steps = bfs_pancake(start)
print("Steps:")
for step in steps:
    print(step)

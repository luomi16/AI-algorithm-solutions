# Import Libraries
# 导入库:
# collections.deque 用于实现双端队列，以便于广度优先搜索(BFS)。
# heapq 用于实现堆队列，以便于A*搜索算法。
from collections import deque
from heapq import heappop, heappush

# Pancake Flipping Function
# 翻转函数(flip):
# flip(s, i) 函数接收两个参数：当前状态 s 和翻转点 i。
# 它通过翻转前 i 个煎饼（从顶部开始）来生成新的状态。


def flip(s, i):
    flipped = ""
    for j in range(0, 2*i, 2):
        number = s[j]
        color = 'w' if s[j+1] == 'b' else 'b'
        flipped = number + color + flipped
    return flipped + s[2*i:]

# Heuristic Function
# 启发式函数(heuristic):

# heuristic(state) 函数计算当前状态 state 到目标状态的启发式估计值，即当前状态下每个煎饼位置错误的数量。


def heuristic(state):
    goal = ''.join([str(i) for i in range(1, len(state) // 2 + 1)])
    actual = ''.join([state[i] for i in range(0, len(state), 2)])
    return sum(1 for a, b in zip(goal, actual) if a != b)

# 状态标识函数(get_id):
# get_id(state) 函数将状态 state 转换为一个整数ID，以便于在搜索过程中快速比较和访问。


def get_id(state):
    return int(state.replace('w', '1').replace('b', '0'))

# BFS Search Function
# BFS搜索函数(bfs_pancake):

# bfs_pancake(start) 函数接收初始状态 start，
# 并使用广度优先搜索(BFS)算法来找到从初始状态到目标状态的路径。


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
# A*搜索函数(a_star_pancake):

# a_star_pancake(start) 函数接收初始状态 start，并使用A*搜索算法来找到从初始状态到目标状态的路径。
# 这个函数使用启发式函数 heuristic 来估计剩余的路径成本，并使用优先队列（通过 heapq 实现）来确定下一个要访问的状态。


def a_star_pancake(start):
    goal = start.replace("b", "w")
    visited = set()
    queue = [(heuristic(start), 0, get_id(start), start, [])]

    while queue:
        f, g, state_id, state, path = heappop(queue)

        if state == goal:
            return path + [(state, g, f - g)]

        for i in range(1, len(start) // 2 + 1):
            new_state = flip(state, i)
            if new_state not in visited:
                visited.add(new_state)
                h = heuristic(new_state)
                new_g = g + i
                new_path = path + [(state[:2*i] + "|" + state[2*i:], g, f - g)]
                new_id = get_id(new_state)
                heappush(queue, (h + new_g, new_g, new_id, new_state, new_path))

    return []

# 主程序:

# 主程序从用户接收输入，判断应该使用哪种搜索算法（BFS 或 A*），然后调用相应的函数来获取从初始状态到目标状态的路径，并打印出路径的步骤。


start_input = input()
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

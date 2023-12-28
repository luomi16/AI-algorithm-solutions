import numpy as np
import random

# Initialize parameters
alpha = 0.3  # Learning rate
gamma = 0.1  # Discount factor
epsilon = 0.5  # Exploration rate
max_iterations = 100000
np.random.seed(1)

# Actions dictionary
actions = {0: 'up', 1: 'right', 2: 'down', 3: 'left'}

# Initialize Q-table
Q = np.zeros((16, 4))


def get_next_state(state, action):
    next_state = state
    if action == 0:  # up
        next_state = state if state > 12 else state + 4
    elif action == 1:  # right
        next_state = state if state % 4 == 0 else state + 1
    elif action == 2:  # down
        next_state = state if state < 5 else state - 4
    elif action == 3:  # left
        next_state = state if state % 4 == 1 else state - 1

    if next_state in [wall]:
        next_state = state
    # Ensure that next_state is within the valid range
    return max(1, min(next_state, 16))

# Function to choose an action based on epsilon-greedy policy


def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return np.random.choice(4)  # Random action
    else:
        return np.argmax(Q[state-1])  # Best action based on current Q-values

# Main Q-learning function


def q_learning(start, goal1, goal2, forbidden, wall):
    for _ in range(max_iterations):
        state = start
        while state not in [goal1, goal2, forbidden]:
            action = choose_action(state)
            next_state = get_next_state(state, action)

            q_state = state - 1
            q_next_state = next_state - 1

            # Adjusting reward values
            if next_state == goal1 or next_state == goal2:
                reward = 100.0  # Higher reward for reaching a goal
            elif next_state == forbidden:
                reward = -100.0  # Negative reward for forbidden state
            elif next_state == wall:
                reward = -0.01
            elif next_state == state:
                reward = -0.1
            else:
                reward = -0.1

            if q_next_state >= 0 and q_next_state < len(Q):
                Q[q_state, action] = Q[q_state, action] + alpha * (
                    reward + gamma * np.max(Q[q_next_state]) - Q[q_state, action])

            state = next_state if next_state != wall else state


def print_policy():
    for i in range(1, 17):
        if i in [goal1, goal2, forbidden, wall]:
            if i == goal1:
                print(f"{i}    goal")
            elif i == goal2:
                print(f"{i}    goal")
            elif i == forbidden:
                print(f"{i}    forbid")
            elif i == wall:
                print(f"{i}    wall-square")
            continue
        print(f"{i}    {actions[np.argmax(Q[i-1])]}")


# Function to print Q-values for a state
# def print_q_values(state):
#     for a in range(4):
#         print(f"{actions[a]}    {Q[state, a]:.2f}")

def print_q_values(state):
    for a in range(4):
        value = Q[state, a]
        formatted_value = f"{value:.2f}"
        if formatted_value[-1] == '0':
            formatted_value = f"{value:.1f}"
        print(f"{actions[a]}    {formatted_value}")


# Input parsing and execution
input_data = input().split()
goal1, goal2, forbidden, wall = map(int, input_data[:4])
output_format = input_data[4]
start = 2

q_learning(start, goal1, goal2, forbidden, wall)
# epsilon = 0  # Set epsilon to 0 after training

if output_format == 'p':
    print_policy()
elif output_format == 'q':
    state_query = int(input_data[5]) - 1
    print_q_values(state_query)

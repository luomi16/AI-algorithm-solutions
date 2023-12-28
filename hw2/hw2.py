def alphabeta(depth, node_index, maximizing_player, values, alpha, beta, visited_nodes):
    if depth == 3:
        visited_nodes.add(node_index)
        return values[node_index]

    num_children = 3 if depth == 0 else 2

    if maximizing_player:
        return max_value(depth, node_index, values, alpha, beta, visited_nodes, num_children)
    else:
        return min_value(depth, node_index, values, alpha, beta, visited_nodes, num_children)


def max_value(depth, node_index, values, alpha, beta, visited_nodes, num_children):
    value = float('-inf')

    for i in range(num_children):
        value = max(value, alphabeta(depth + 1, (node_index * num_children) + i, False, values, alpha, beta, visited_nodes))
        alpha = max(alpha, value)

        if beta <= alpha:
            break

    return value


def min_value(depth, node_index, values, alpha, beta, visited_nodes, num_children):
    value = float('inf')

    for i in range(num_children):
        value = min(value, alphabeta(depth + 1, (node_index * num_children) + i, True, values, alpha, beta, visited_nodes))
        beta = min(beta, value)

        if beta <= alpha:
            break

    return value


if __name__ == "__main__":
    values_input = list(map(int, input().split()))
    visited_nodes = set()
    alphabeta(0, 0, True, values_input, float('-inf'), float('inf'), visited_nodes)
    
    pruned = [i for i in range(12) if i not in visited_nodes]
    print(" ".join(map(str, pruned)))

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# input: triple
# output: w
def perceptron(inputs):
    w = np.array([0.0, 0.0])
    for _ in range(100):
        for x1, x2, y in inputs:
            prediction = 1 if w[0]*x1 + w[1]*x2 >= 0 else -1
            if prediction != y:
                w[0] += y * x1
                w[1] += y * x2
    return w

# input: triple
# output: probability
def logistic_regression(inputs):
    w = np.array([0.0, 0.0])
    alpha = 0.1
    for _ in range(100):
        for x1, x2, y in inputs:
            x = np.array([x1, x2])
            z = np.dot(w, x)
            prediction = sigmoid(z)
            error = prediction - y
            w -= alpha * error * x

    probabilities = [sigmoid(np.dot(w, [x1, x2])) for x1, x2, _ in inputs]
    return [round(p, 2) for p in probabilities]

def parse_input(input_str, type_of_algorithm):
    data = []
    parts = input_str.split(') ')
    for part in parts:
        numbers = part.split(',')
        x1 = float(numbers[0].strip('P (L '))
        x2 = float(numbers[1])
        if type_of_algorithm == 'P':
            y = 1 if '+1' in numbers[2] else -1
        elif type_of_algorithm == 'L':
            y = 1.00 if '+1' in numbers[2] else 0.00
        data.append((x1, x2, y))
    return data

def main():
    input_str = input()
    type_of_algorithm = input_str[0]
    data = parse_input(input_str[1:], type_of_algorithm)

    if type_of_algorithm == 'P':
        w = perceptron(data)
        print(f"{w[0]:.1f}, {w[1]:.1f}")
    elif type_of_algorithm == 'L':
        probabilities = logistic_regression(data)
        formatted_probabilities = []
        for p in probabilities:
            formatted_p = f"{p:.2f}"
            if formatted_p[-1] == '0':
                formatted_p = f"{p:.1f}"
            formatted_probabilities.append(formatted_p)
        print(' '.join(formatted_probabilities))

if __name__ == "__main__":
    main()

import numpy as np

def main():
    random_matrix = generate_random_matrix(4, 5)

    mat_matrix(random_matrix)

    print("Modified Matrix:")
    print(random_matrix)

def generate_random_matrix(rows, cols):
    return np.random.uniform(1, 20, size=(rows, cols))

def mat_matrix(matrix):
    matrix[np.arange(matrix.shape[0]), matrix.argmax(axis=1)] = 0

if __name__ == "__main__":
    main()

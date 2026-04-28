import numpy as np

def test_matrix_addition():
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])

    B = np.array([[6, 5, 4],
                  [3, 2, 1]])

    C = A + B

    assert C[0][0] == 7
    assert C[1][2] == 7


def test_column_average():
    C = np.array([[7, 7, 7],
                  [7, 7, 7]])

    col_means = C.mean(axis=0)

    assert col_means[0] == 7

import numpy as np

def main():
    try:
        #мій номер залікової 5202
        num = 5202

        #обрахунок остачі
        C5 = num % 5
        C7 = num % 7
        C11 = num % 11

        print("C5 =", C5)
        print("C7 =", C7)
        print("C11 =", C11)

        #створення 2 матриць а та б
        A = np.array([
            [1, 2, 3],
            [4, 5, 6]
        ], dtype=int)

        B = np.array([
            [6, 5, 4],
            [3, 2, 1]
        ], dtype=int)


        print("\nMatrix A:\n", A)
        print("\nMatrix B:\n", B)

        if C5 == 0:
            a = 2
            C = a * B

        elif C5 == 1:
            C = B.T

        elif C5 == 2:
            C = A + B

        elif C5 == 3:
            C = np.bitwise_xor(A, B)

        elif C5 == 4:
            C = np.matmul(A, B)

        else:
            raise ValueError("Невірне значення C5")

        print("\nПерша операція матриця C:\n", C)

        if C7 == 0:
            dtype = float
            type_name = "double"
        elif C7 == 1:
            dtype = int  # byte (імітація)
            type_name = "byte"
        elif C7 == 2:
            dtype = int  # short (імітація)
            type_name = "short"
        elif C7 == 3:
            dtype = int
            type_name = "int"
        elif C7 == 4:
            dtype = int  # long (в Python немає різниці)
            type_name = "long"
        elif C7 == 5:
            dtype = str  # char
            type_name = "char"
        elif C7 == 6:
            dtype = float
            type_name = "float"

        print("Тип елементів матриці", type_name)

        if C11 == 0:
            result = np.sum(np.min(C, axis=0))

        elif C11 == 1:
            result = np.sum(np.min(C, axis=1))

        elif C11 == 2:
            result = np.sum(np.max(C, axis=0))

        elif C11 == 3:
            result = np.sum(np.max(C, axis=1))

        elif C11 == 4:
            result = 0
            for i in range(len(C)):
                if i % 2 == 0:
                    result += np.max(C[i])
                else:
                    result += np.min(C[i])

        elif C11 == 5:
            result = 0
            for i in range(len(C)):
                if i % 2 == 0:
                    result += np.min(C[i])
                else:
                    result += np.max(C[i])

        elif C11 == 6:
            result = 0
            for j in range(C.shape[1]):
                col = C[:, j]
                if j % 2 == 0:
                    result += np.max(col)
                else:
                    result += np.min(col)

        elif C11 == 7:
            result = 0
            for j in range(C.shape[1]):
                col = C[:, j]
                if j % 2 == 0:
                    result += np.min(col)
                else:
                    result += np.max(col)

        elif C11 == 8:
            result = np.mean(C, axis=1)

        elif C11 == 9:
            result = np.mean(C, axis=0)

        elif C11 == 10:
            result = np.mean(C)

        else:
            raise ValueError("Невірне значення C11")

        print("\nДруга операція матриця С:")
        print(result)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()

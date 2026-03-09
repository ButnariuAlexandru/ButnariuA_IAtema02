import numpy as np

def genM (linii, coloane, low=0, high=10):
    np.random.seed(12)

    if not isinstance(linii, int) or not isinstance(coloane, int):
        raise TypeError("linii si coloane trebuie sa fie intregi")

    
    matrix = np.random.randint(low, high, (linii, coloane))
    return matrix

def main():
    low = 0
    high = 10

    matrixA = genM(4, 3, low, high)
    print("Matrix A:")
    print(matrixA)

    matrixB = genM(3, 5, low, high)
    print("Matrix B:")
    print(matrixB)

    matrixC = matrixA @ matrixB
    print("Matrix C (A @ B):")
    print(matrixC)

    sum=0
    for i in range(matrixC.shape[0]):
        for j in range(matrixC.shape[1]):
            sum += matrixC[i, j]
    print(f"Suma tuturor elementelor este: {sum}")

    for j in range(matrixC.shape[1]):
        col_sum = 0
        for i in range(matrixC.shape[0]):
            col_sum += matrixC[i, j]
        media = col_sum / matrixC.shape[0]
        print(f"Media coloanei {j} este: {media}")

    max_val = matrixC.max()
    print(f"Valoarea maxima din matrice este: {max_val}")

    matrixM = genM(3, 3, low, high)
    print("Matrix M:")
    print(matrixM)

    matrixInv = np.linalg.inv(matrixM)
    print("Inversa matricei M:")
    print(matrixInv)

    matrixDet = np.linalg.det(matrixM)
    print(f"Determinantul matricei M: {matrixDet}")

    identity = matrixM @ np.linalg.inv(matrixM)
    print("M @ M^-1 (ar trebui sa fie matricea identitate):")
    is_identity = np.allclose(identity, np.eye(3), atol=1e-8)
    print(f"Este matricea identitate? {is_identity}")


if __name__ == "__main__":
    main()
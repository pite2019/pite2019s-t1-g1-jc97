from matrix import Matrix

matrixA = Matrix(2, 2)
matrixB = Matrix(2, 2)

matrixA.setValues([[1, 2], [3, 4]])
matrixB.setValues([[5, 6], [7, 8]])

matrixC = matrixB - matrixA

matrixC.printMatrix()
print("");
matrixC -= 3
matrixC.printMatrix()
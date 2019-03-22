from matrix import *

matrixA = Matrix(2, 2)
matrixB = Matrix(2, 2)

matrixA.setValues([[1, 2], [3, 4]])
matrixA.setValues([[5, 6], [7, 8]])

matrixA.printMatrix()
matrixB.printMatrix()

matrixA.add(MatrixB)

matrixA.printMatrix()

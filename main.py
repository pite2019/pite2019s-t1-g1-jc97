from matrix import Matrix

matrixA = Matrix(2, 3)
matrixB = Matrix(2, 3)

matrixA.set_values([[10, 20, 100], [30, 40.2, 110]])
matrixB.set_values([[5, 6, 200], [7, 8, 300]])

matrixC = matrixB - matrixA

matrixC.print_matrix()

matrixC = 2 - matrixC
matrixC.print_matrix()

for line in matrixC:
	print(line)

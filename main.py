from matrix import Matrix

matrixA = Matrix(2, 3)
matrixB = Matrix(2, 3)

matrixA.set_values([[10, 20, 100], [30, 40.2, 110]])
matrixB.set_values([[5, 6, 200], [7, 8, 300]])
matrixA.print_matrix()

matrixC = matrixB - matrixA

matrixC.print_matrix()

matrixC = 2 - matrixC
matrixC.print_matrix()

for line in matrixC:
	print(line)

print("")
print("Test mul:")

matrixD = Matrix(2, 3)
matrixE = Matrix(3, 2)

matrixD.set_values([[2, 3, 4], [3, 4, 5]])
matrixE.set_values([[3, 2], [4, 4], [1, 5]])

matrixF = matrixD.multiply(matrixE)
matrixF.print_matrix()

print("")

matrixD @= matrixE
matrixD.print_matrix()

print("")

x = 2
x @= matrixA
x.print_matrix()

print("")
print("Test vectors:")
print("")

vectorA = Matrix(1, 4)
vectorA.set_values([[2, 3, 4, 5]])
vectorB = Matrix(4, 1)
vectorB.set_values([[3], [4], [5], [6]])

(vectorB @ vectorA).print_matrix()

#!/usr/bin/python3

from typing import List


class Matrix:
    __lines = ... # type: int
    __columns = ... # type: int
    __matrix = ... # type: List[List[int]]

    def __init__(self, lines, columns):
        if not isinstance(lines, int) or lines < 2 or not isinstance(columns, int) or columns < 2:
            raise ValueError()
        self.__lines = lines
        self.__columns = columns
        self.__matrix = []
        for i in range(0, columns):
            self.__matrix[i] = []
            for j in range(0, lines):
                self.__matrix[i][j] = 0

    @property
    def lines(self):
        return 


    def setColumn(self, column, values):
        if not isinstance(column, int) or column >= self.__columns:
            raise ValueError()
        if not isinstance(values, List) or len(values) != self.__lines:
            raise ValueError()
        self.__matrix[column] = values

    def setValues(self, values):
        if not isinstance(values, List) or len(values) != self.__lines:
			raise ValueError()
		for line in values:
			if not isinstance(line, List) or len(line) != self.__columns:
				raise ValueError()
			for value in line:
				if not isinstance(value, int):
					raise ValueError()
		self.__matrix = values

	def addMatrix(self, matrix):
		if not isinstance(matrix, Matrix) or matrix.__lines != self.__lines or matrix.__columns != self.__columns:
			raise ValueError()
		for i in range(0, self.__columns):
			for j in range(0, self.__lines):
				self.__matrix[i][j] = matrix[i][j]
	
	def printMatrix(self):
		for j in range(0, self.__lines):
			for i in range(0, self.__columns):
				print(str(self.__matrix[i][j]) + " ")
			print("\n")


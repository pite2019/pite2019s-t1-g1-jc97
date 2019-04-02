#!/usr/bin/python3

from typing import List


class Matrix:
	__lines = ...  # type: int
	__columns = ...  # type: int
	__matrix = ...  # type: List[List[int]]

	def __init__(self, lines, columns):
		if not isinstance(lines, int) or lines < 2 or not isinstance(columns, int) or columns < 2:
			raise ValueError()
		self.__lines = lines
		self.__columns = columns
		self.__matrix = []
		self.__num = 0
		for i in range(0, lines):
			self.__matrix.append([])
			for j in range(0, columns):
				self.__matrix[i].append(0)

	def set_values(self, values):
		if not isinstance(values, List) or len(values) != self.__lines:
			raise ValueError()
		for line in values:
			if not isinstance(line, List) or len(line) != self.__columns:
				raise ValueError()
			for value in line:
				if not isinstance(value, int) and not isinstance(value, float):
					raise ValueError()
		self.__matrix = values

	def add_matrix(self, summand):
		if not isinstance(summand, Matrix) or summand.__lines != self.__lines or summand.__columns != self.__columns:
			raise ValueError()
		for i in range(0, self.__lines):
			for j in range(0, self.__columns):
				self.__matrix[i][j] += summand.__matrix[i][j]

	def subtract_matrix(self, subtrahend):
		if not isinstance(subtrahend, Matrix) or subtrahend.__lines != self.__lines or subtrahend.__columns != self.__columns:
			raise ValueError()
		for i in range(0, self.__lines):
			for j in range(0, self.__columns):
				self.__matrix[i][j] += subtrahend.__matrix[i][j]

	def __add__(self, summand):
		numeric_summand = False
		if isinstance(summand, float) or isinstance(summand, int):
			numeric_summand = True
		elif not isinstance(summand, Matrix) or summand.__lines != self.__lines or summand.__columns != self.__columns:
			raise ValueError()
		result = Matrix(self.__lines, self.__columns)
		for i in range(0, self.__lines):
			for j in range(0, self.__columns):
				if numeric_summand:
					result.__matrix[i][j] = self.__matrix[i][j] + summand
				else:
					result.__matrix[i][j] = summand.__matrix[i][j] + self.__matrix[i][j]
		return result

	def __radd__(self, other):
		return self.__add__(other)

	def __sub__(self, subtrahend, invert=False):
		numeric_subtrahend = False
		if isinstance(subtrahend, float) or isinstance(subtrahend, int):
			numeric_subtrahend = True
		elif not isinstance(subtrahend, Matrix) or subtrahend.__lines != self.__lines \
			or subtrahend.__columns != self.__columns:
			raise ValueError()
		result = Matrix(self.__lines, self.__columns)
		for i in range(0, self.__lines):
			for j in range(0, self.__columns):
				if numeric_subtrahend:
					result.__matrix[i][j] = (self.__matrix[i][j] - subtrahend) * (-1 if invert else 1)
				else:
					result.__matrix[i][j] = (self.__matrix[i][j] - subtrahend.__matrix[i][j]) * (-1 if invert else 1)
		return result
	
	def __rsub__(self, other):
		return self.__sub__(other, True)

	def print_matrix(self):
		for i in range(0, self.__lines):
			for j in range(0, self.__columns):
				print(str(self.__matrix[i][j]) + " ", end='')
			print("\n", end='')
		print("")

	def __iter__(self):
		return self

	def __next__(self):
		if self.__num < self.__lines:
			self.__num += 1
			return self.__matrix[self.__num - 1]
		else:
			raise StopIteration()

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	ans = [[y*scalar for y in x] for x in matrix]
	return ans
	
import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1. 
	if len(a[0]) != len(b) :
		return -1 
	ans = []
	b_np = np.array(b)
	for i in range(len(b)):
		a_np = np.array(a[i])
		
		ans.append(np.dot(a_np,b_np))
	return ans
	
	
import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
    if len(a[0]) != len(b):
        return -1 

    a_np = np.array(a)
    b_np = np.array(b)  
    c_np = a_np @ b_np 
    c = c_np.tolist()
    return c
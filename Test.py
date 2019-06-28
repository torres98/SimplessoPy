import numpy as np
from Simplex import simplex
from Simplex_main import simplex_main

A=np.array([[1,2,3,1], [2,1,1,2]])
base=np.array([[2,1],[1,2]])
b=np.array([3, 4])
c=np.array([1,3,5,2])
var_base=np.array([2,4])

ott = simplex_main(A,b,c, True)
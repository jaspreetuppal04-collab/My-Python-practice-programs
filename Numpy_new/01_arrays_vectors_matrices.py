import numpy as np

vector_row = np.array([1,2,3])
vector_column = np.array([[1],[2],[3]])
matrix = np.array([[2,4,5],
                   [6,7,1]])

print(vector_row,"\n")
print(vector_column,"\n")
print(matrix)


from scipy import sparse
matrix_large = np.array([ [1,0,1,0,0,0,1,1,1,0,0],
                  [0,0,0,0,0,0,0,0,0,0,0],
                  [0,1,1,0,1,0,1,0,0,0,0]])
matrix_large_sparse = sparse.csr_matrix(matrix_large)

print(matrix_large_sparse)
print(matrix_large.shape)
print(matrix_large_sparse.shape)
# load libraries
import scipy.sparse as sparse
from sklearn.decomposition import TruncatedSVD

def SVD(N,matrix):
    '''
    Singular Value Decomposition
    '''
    svd = TruncatedSVD(n_components=N)
    matrix_sparse = sparse.lil_matrix(matrix)
    matrix_svd = svd.fit_transform(matrix_sparse)
    return matrix_svd
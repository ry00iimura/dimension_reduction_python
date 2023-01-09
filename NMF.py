# load the libraries
from sklearn.decomposition import NMF
import scipy.sparse as sparse

def NMF(N,matrix):
    '''
    Non Negative Matrix Factorization
    '''
    nmf = NMF(n_components=N, random_state = 1234, init = 'random')
    matrix_sparse = sparse.lil_matrix(matrix)
    matrix_nmf = nmf.fit_transform(matrix_sparse)
    return matrix_nmf
# Dependencies:
import numpy as np
import numpy.ma as ma
import pytest
from ustat.sampc import sampc
from ustat.makec import makec
from ustat.lamb_sum import lamb_sum
from ustat.ustat_samp_covar import ustat_samp_covar
from ustat.generate_test_data import generate_unique_nan_arrays
from ustat.generate_test_data import generate_data


def test_ustat_samp_covar_sym_balanced():
    ''' Test that Ustat gives symmetric results on simple, balanced arrays with no NaNs '''
    
    # Arrays to test
    A = np.array([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [3.0, 2.0, 1.0]
    ])
    B = np.array([
        [1.0, 2.0, 3.0],
        [6.0, 5.0, 4.0],
        [64.0, 8.0, 1.0]
    ])
    C = np.array([
        [1.0, 2.0, 3.0],
        [5.0, 4.0, 3.0],
        [6.0, 5.50, 5.0]
    ])
    D = np.array([
        [1.0, 2.0, 3.0],
        [7.0, 5.0, 3.0],
        [9.0, 1.0, 81.0]
    ])
    
    # Two types of symmetry tests:
    # - Cov(Cov(A,B), Cov(C,D)) = Cov(Cov(C,D), Cov(A,B))
    # - Cov(Cov(B,A), Cov(D,C)) = Cov(Cov(A,B), Cov(C,D))
    # If both are true, then all symmetry relations are true.
    np.testing.assert_allclose(ustat_samp_covar(A, B, C, D), ustat_samp_covar(C, D, A, B), rtol=1e-6)
    np.testing.assert_allclose(ustat_samp_covar(B, A, D, C), ustat_samp_covar(A, B, C, D), rtol=1e-6)


def test_ustat_samp_covar_sym_unbalanced():
    ''' Test that Ustat gives symmetric results on simple, unbalanced arrays with NaNs '''
    
    # (Fixed) random arrays to test
    # We use the random arrays because we can get an arbitrary degree of unbalancedness across teachers.
    A, B, C, D = generate_unique_nan_arrays(n_rows = 100, n_cols = 50, n_arrays = 4,
                                            min_int=1, max_int = 100, nan_prob = 0.25, seed = 14378,
                                            balanced = False)
    
    # Two types of symmetry tests:
    # - Cov(Cov(A,B), Cov(C,D)) = Cov(Cov(C,D), Cov(A,B))
    # - Cov(Cov(B,A), Cov(D,C)) = Cov(Cov(A,B), Cov(C,D))
    # If both are true, then all symmetry relations are true.
    np.testing.assert_allclose(ustat_samp_covar(A, B, C, D), ustat_samp_covar(C, D, A, B), rtol=1e-6)
    np.testing.assert_allclose(ustat_samp_covar(B, A, D, C), ustat_samp_covar(A, B, C, D), rtol=1e-6)


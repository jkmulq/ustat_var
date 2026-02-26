# Dependencies
import numpy as np


def varcovar_balanced(origX,origY, w = None, quiet = False, homoskedastic_noise = False):

    # Check if user supplied weights.
    # If they exist, describe what type of weights they are
    if not(w is None):
        weights = w
        if (weights.ndim != 1):
            ValueError("Supplied weights have strange dimension. The 'w' object needs to be an array with J elements, where J is the number of rows in A and B. Inspect and retry.")
        
        if np.any(weights < 0):
            raise ValueError("Supplied weights have negative values. Please inspect and try again.")
    
    ## 1 Input checks ##
    # Check if X, Y have observations
    if (len(origX) == 0) | (len(origY) == 0):
        print('No observations in X or Y matrices')
        return np.nan
    
    # Function does not support X_{jt} = 0 (since these are indistinguishable from NaN/missing values).
    # Raise error if 0 value detected.
    if (np.sum(origX == 0) != 0) | (np.sum(origY == 0) != 0):
        raise ValueError("Supplied data has at least 1 data point which =0. 0 data points are not supported. Please inspect and try again.")
    
    # check that each teacher appear at least 2 times in each matrix
    if (origX.shape[1] < 2) | (origY.shape[1] < 2):
        raise ValueError("At least one teacher must appear at least 2 times in each matrix. Please inspect and try again.")

    # Impose that both "Y" and "X" outcomes appear in year "t" --- this is needed here but not in the U-stat version
    #   check if this is the case and if not impose it
    check_balance = np.sum((np.isnan(origX) == np.isnan(origY)).all())
    if (check_balance == 0):
        unbalanced_teachers = ((np.isnan(origX) == np.isnan(origY)) == False).sum(axis=1)
        # keep only teachers that appear in both X and Y
        origX = origX[np.where(unbalanced_teachers==0), :] 
        origY = origY[np.where(unbalanced_teachers==0), :]
    check_balance = np.sum((np.isnan(origX) == np.isnan(origY)).all())
    assert check_balance == 1

    ## 2 Compute necessary values ## 
    # Counds of valid obs
    countsX = np.count_nonzero(~np.isnan(origX),1)  # No. of obs in X
    countsY = np.count_nonzero(~np.isnan(origY),1)  # No. of obs in Y
    nsquares = np.count_nonzero(~np.isnan(origX * origY),1)   # No. of obs in both X and Y
    nproducts = (countsX*countsY - nsquares) # No. of valid product pairs
    X = np.nan_to_num(origX[nproducts > 0, :].copy(), 0) # Create X, which is copy of origX, though removing teachers who only have 1 observation on a specific outcome.
    Y = np.nan_to_num(origY[nproducts > 0, :].copy(), 0) # Same for Y and origY here. In  both, we replace NaNs with 0. 
    
    # If weights present, drop those rows with only one observation too
    if not(w is None):
        weights = w[nproducts > 0].copy()
        
    # Report back to user how many rows were dropped due (if they were dropped)
    drop_row_check = np.any(nproducts == 0)
    if (drop_row_check):
        n_dropped = np.sum(nproducts == 0)
        if not(quiet):
            print(str(n_dropped) + " rows dropped due to having no valid observations across both outcomes.")
    
    J = X.shape[0]# total number of teachers

    if (len(X) == 0) | (len(Y) == 0):
        print('No observations in X or Y vectors')
        return np.nan

    # Calculate within-teacher covariances
    Xdemeans = X - (X.sum(axis=1)/np.count_nonzero(X, axis=1))[:,np.newaxis]
    Xdemeans = Xdemeans * (X!=0)
    Ydemeans = Y - (Y.sum(axis=1)/np.count_nonzero(Y, axis=1))[:,np.newaxis]
    Ydemeans = Ydemeans * (Y!=0)
    covs_j = (Xdemeans*Ydemeans).sum(axis=1)/(np.count_nonzero(X, axis=1)-1)
    covs_j = covs_j/np.count_nonzero(X, axis=1) 

    if homoskedastic_noise:
        covs_homo = (Xdemeans*Ydemeans).sum()/(np.count_nonzero(X)-1)
        covs_j_homo = covs_homo/np.count_nonzero(X, axis=1)

    # Calculate ACROSS teacher covariance
    Xmeans = X.sum(axis=1)/np.count_nonzero(X, axis=1)
    Ymeans = Y.sum(axis=1)/np.count_nonzero(Y, axis=1)
    
    if not(w is None):
        weights_norm = weights / np.sum(weights)
        Xmeans = Xmeans - (Xmeans*weights_norm).sum()
        Ymeans = Ymeans - (Ymeans*weights_norm).sum()
        for_covs_across = Xmeans * Ymeans
        covs_across = (for_covs_across*weights_norm).sum()
        sampling_var = (covs_j*weights_norm*(1-weights_norm)).sum()
    else:
        Xmeans = Xmeans - Xmeans.sum()/J    
        Ymeans = Ymeans - Ymeans.sum()/J
        covs_across = (Xmeans * Ymeans).sum()/J
        covs_j = covs_j*(1-1/J)
        sampling_var = covs_j.sum()/J
    
    if homoskedastic_noise:
        if not(w is None):
            sampling_var_homo = (covs_j_homo*weights_norm*(1-weights_norm)).sum()
        else:
            covs_j_homo = covs_j_homo*(1-1/J)
            sampling_var_homo = covs_j_homo.sum()/J
        debias_varcovar = covs_across - sampling_var_homo
    else:
        debias_varcovar = covs_across - sampling_var

    return debias_varcovar

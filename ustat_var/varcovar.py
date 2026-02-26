# Dependencies:
import numpy as np

# U-stat estimator of variance / covariance
def varcovar(origX, origY, w=None, quiet=True):
    r'''
    U-stat estimator of variance / covariance for teacher effects
    X and Y are a J-by-:math:`\operatorname{max}(T_j)` matrix of teacher-specific mean residuals. 
    When X and Y are residuals for the same outcome and covariate group,
    code will return a estimate of variance of teacher effects. When X and Y
    differ (either in outcome or Xs), code returns an estimate of the 
    covariance. 

    Each row of X and Y are residuals for a specific teacher, ordered as
    first year observed, second year observed, etc. Since teachers have
    different number of years observed, X and Y should be np.NaN for all
    years after the last year observed. Each teacher must have at least
    2 years observed.

    X and Y must have the same dimension.

    Note, this is a warrpper function that calls varcovar_balanced or varcovar_ustat depending on whether the panels are balanced or unbalanced.
   "varcovar_balanced.py" is used when the panels are balanced, i.e. each teacher appears the same number of times in both X and Y.
    "varcovar_ustat.py" is used when the panels are unbalanced, i.e. each teacher appears a different number of times in X and Y.
    
    Parameters
    ----------
    origX: array
        J-by-:math:`\operatorname{max}(T_j)` array containing residuals/data for outcome X
    origY: array
        J-by-:math:`\operatorname{max}(T_j)` array containing residuals/data for outcome Y
    w: array
        (Optional) J-by-1 array of user-supplied weights. If supplied, varcovar will return row-weighted variance-covariance of row means. 
    quiet: boolean
        (Optional) If quiet=True, function call will report type of variance being calculated (unweighted/weighted) and whether panels are balanced or unbalanced.

    Returns
    -------
    float
        Variance-covariance between rowmeans of origX and origY.
    '''
    
    ## 1 Input checks ##
    # Check if X, Y have observations
    if (len(origX) == 0) | (len(origY) == 0):
        print('No observations in X or Y matrices')
        return np.nan
    
    # Check if user supplied weights.
    # If they exist, describe what type of weights they are
    if not(w is None):
        weights = w
        if (weights.ndim != 1):
            ValueError("Supplied weights have strange dimension. The 'w' object needs to be an array with J elements, where J is the number of rows in A and B. Inspect and retry.")
        
        if np.any(weights < 0):
            raise ValueError("Supplied weights have negative values. Please inspect and try again.")
    
    # Function does not support X_{jt} = 0 (since these are indistinguishable from NaN/missing values).
    # Raise error if 0 value detected.
    if (np.sum(origX == 0) != 0) | (np.sum(origY == 0) != 0):
        raise ValueError("Supplied data has at least 1 data point which =0. 0 data points are not supported. Please inspect and try again.")
    
    # check that each teacher appear at least 2 times in each matrix
    if (origX.shape[1] < 2) | (origY.shape[1] < 2):
        raise ValueError("At least one teacher must appear at least 2 times in each matrix. Please inspect and try again.")
    
    # Check if panels are balanced/unbalanced
    check_balance = np.sum((np.isnan(origX) == np.isnan(origY)).all())
    if check_balance == 1:
        Ustat_estimate = varcovar_balanced(origX, origY, w, quiet)
    else:
        Ustat_estimate = varcovar_ustat(origX, origY, w, quiet)
    
    return Ustat_estimate


    

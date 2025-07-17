# Dependencies:
import numpy as np
from .sampc import sampc
from .makec import makec
from .lamb_sum import lamb_sum

# Estimate the sampling covariance between two sampling estimates
def ustat_samp_covar(Atmp,Btmp,Ctmp,Dtmp, w=None):
    '''
    Estimate the sampling covariance between the estimate of 
    Cov(Atmp,Btmp) and the estimates of Cov(Ctmp,Dtmp).

    By setting Atmp=Btmp=Ctmp=Dtmp, for example, one will simply 
    get the sampling variance of a variance estimate.
    
    row-wise/teacher-level weights (optional)
    '''
    # Make copies
    A = Atmp.copy()
    B = Btmp.copy()
    C = Ctmp.copy()
    D = Dtmp.copy()

    # Compute sampling covariances
    sigAC = sampc(A,C) # These are standard formulae; i.e., sampc(X, Y) = (X - Xmean) * (Y - Ymean) / (|XY| - 1)
    sigAD = sampc(A,D)
    sigBC = sampc(B,C)
    sigBD = sampc(B,D)

    # Counts
    # Count the cardinality of the intersections between matrices A and C, and so on.
    countsAC = np.array(np.sum(~np.isnan(A) & ~np.isnan(C), axis=1),dtype=float) 
    countsAD = np.array(np.sum(~np.isnan(A) & ~np.isnan(D), axis=1),dtype=float)
    countsBC = np.array(np.sum(~np.isnan(B) & ~np.isnan(C), axis=1),dtype=float)
    countsBD = np.array(np.sum(~np.isnan(B) & ~np.isnan(D), axis=1),dtype=float)
    countsABCD = np.array(np.sum(~np.isnan(A) & ~np.isnan(C)
                    & ~np.isnan(B) & ~np.isnan(D), axis=1),dtype=float)

    # Compute Ciks.
    if (w is None):
        # Compute unweighted C coefficients
        
        C_jjAB, C_jkAB = makec(A,B)
        C_jjCD, C_jkCD = makec(C,D)
        C_jjBA, C_jkBA = makec(B,A) # Add reverse
        C_jjDC, C_jkDC = makec(D,C)
    
    elif:
        # Compute j-weighted C coefficient
        C_jjAB, C_jkAB = makec(A,B, w = w)
        C_jjCD, C_jkCD = makec(C,D, w = w)
        C_jjBA, C_jkBA = makec(B,A, w = w) # Add reverse
        C_jjDC, C_jkDC = makec(D,C, w = w)


    # Compute bias corrected products of sums
    prodABBCDD = lamb_sum(B, C_jjAB, C_jkAB, D, C_jjCD, C_jkCD)
    prodABBDCC = lamb_sum(B, C_jjAB, C_jkAB, C, C_jjDC, C_jkDC)
    prodBAACDD = lamb_sum(A, C_jjBA, C_jkBA, D, C_jjCD, C_jkCD)
    prodBAADCC = lamb_sum(A, C_jjBA, C_jkBA, C, C_jjDC, C_jkDC)
    
    # Variance calulation
    vsum = (
            countsAC*sigAC*prodABBCDD +
            countsAD*sigAD*prodABBDCC +
            countsBC*sigBC*prodBAACDD +
            countsBD*sigBD*prodBAADCC 
            )

    # Add last piece
    tmpC = C_jkAB * C_jkDC * sigBC[np.newaxis,:] * countsBC[np.newaxis,:]
    tmpC = (np.sum(tmpC, 1) - np.diag(tmpC))
    vsum += sigAD*countsAD*tmpC
    vsum += sigAD*C_jjAB*C_jjDC*sigBC*(countsAD*countsBC - countsABCD) 

    tmpC = C_jkAB * C_jkCD * sigBD[np.newaxis,:] * countsBD[np.newaxis,:]
    tmpC = (np.sum(tmpC, 1) - np.diag(tmpC))
    vsum += sigAC*countsAC*tmpC
    vsum += sigAC*C_jjAB*C_jjCD*sigBD*(countsBD*countsAC - countsABCD) 

    return np.sum(vsum)

# Dependencies
import numpy as np

# Helper for bias-corrected sum squares
def lamb_sum(X,C_jjX,C_jkX,Y,C_jjY,C_jkY):
    '''
    bias corrected product of (sum_k!=i C_ij^X a^X) (sum_k!=i C_ij^Y a^Y)
    '''
    Xmeans = np.nanmean(X, axis=1)
    Ymeans = np.nanmean(Y, axis=1)    
    Xcounts = np.array(np.sum(~np.isnan(X), axis=1),dtype=float)
    Ycounts = np.array(np.sum(~np.isnan(Y), axis=1),dtype=float)
    Xmeans[Xcounts < 2] = 0 # Why do we do this?
    Ymeans[Ycounts < 2] = 0

    XYcounts = np.array(np.sum(~np.isnan(X) & ~np.isnan(Y), axis=1),dtype=float)
    XYcovar = np.nansum((X-Xmeans[:,np.newaxis])*(Y-Ymeans[:,np.newaxis]),1,dtype=float)/(XYcounts-1) # Standard sampling covariance formula between X and Y.
    XYcovar[XYcounts <= 1] = 0  # No sampling covariance if no overlap

    tmpX = C_jkX*Xmeans[np.newaxis,:]*Xcounts[np.newaxis,:]    
    tmpY = C_jkY*Ymeans[np.newaxis,:]*Ycounts[np.newaxis,:]    
    tmpBXY = C_jkX*C_jkY*XYcovar[np.newaxis,:]*XYcounts[np.newaxis,:]    
    tmpc = (XYcounts - 1)**2/XYcounts
    tmpc[XYcounts == 0] = 0
    return (
                (C_jjX*Xmeans*(Xcounts - 1) + 
                    np.sum(tmpX,1) - np.diag(tmpX))*
                (C_jjY*Ymeans*(Ycounts - 1) + 
                    np.sum(tmpY,1) - np.diag(tmpY))

                - (C_jjX*C_jjY*XYcovar*tmpc + ( # Bias correction
                            np.sum(tmpBXY,1) - np.diag(tmpBXY)))
            )

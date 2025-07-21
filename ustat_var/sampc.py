# Dependencies
import numpy as np

# Helper function for sampling covariances
def sampc(X,Y):
    Xmeans = np.nanmean(X, axis=1)
    Ymeans = np.nanmean(Y, axis=1)
    XYcounts = np.array(np.sum(~np.isnan(X) & ~np.isnan(Y), axis=1),dtype=float)
    XYcovar = np.nansum((X-Xmeans[:,np.newaxis])*(Y-Ymeans[:,np.newaxis]),1,dtype=float)/(XYcounts-1)
    XYcovar[XYcounts <= 1] = 0  
    return XYcovar

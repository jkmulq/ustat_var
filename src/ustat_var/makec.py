# Dependencies
import numpy as np

# Helper for C functions
def makec(X,Y):
    Xcounts = np.array(np.sum(~np.isnan(X), axis=1),dtype=float) # returns no. of observations across all teachers in X (e.g. event X)
    Ycounts = np.array(np.sum(~np.isnan(Y), axis=1),dtype=float) # returns no. of observations across all teachers in Y (e.g. event Y)
    XYcounts = np.array(np.sum(~np.isnan(X) & ~np.isnan(Y), axis=1),dtype=float) # returns no. of observations across all teachers in XandY (e.g. shared observations)
    J = sum(Xcounts*Ycounts - XYcounts > 0) 

    # Compute C coefficients
    C_jj = (J-1)/J**2/(Xcounts*Ycounts - XYcounts)
    C_jj[(Xcounts*Ycounts - XYcounts) == 0] = 0
    C_jk = -1/J**2*(1/Xcounts).reshape(-1,1).dot((1/Ycounts).reshape(1,-1))    # J-by-J, with C_jk as each element.
    
    # Set those with no observations to 0
    C_jk[Xcounts == 0,:] = 0 
    C_jk[:,Ycounts == 0] = 0 

    return C_jj, C_jk

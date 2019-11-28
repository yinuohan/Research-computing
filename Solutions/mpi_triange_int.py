"""
    This code computes the value of the integral:
    $E_{i,j,k} = \sum_{l_1}\sum_{l_2}\sum_{l_3}
    \left( \int_{-1}^{1} d\mu P_{l_1}(\mu) P_{l_2}(\mu)
    P_{l_3}(\mu)\right) X^i_{l_1} X^j_{l_2} X^k_{l_3} $
    
    The code takes some set of $X^i_{l}$ for i element of [0,imax]
    and calculates $E_{i,j,k}$ for every possible triple of [0,imax]
    
    The code works by reordering the integration and sum to form:
    $Y^i(\mu) = \sum_l P_{l}(\mu)  X^i_{l}$
    $E_{i,j,k} = \int_{-1}^{1} d\mu Y^i(\mu)Y^j(\mu)Y^k(\mu)$
    
    The first is computed as a matix product
    The second is computed using Gauss Legendre quadriture
    as it is exact for polynomial arguments
    
    Written by James Fergusson: J.Fergusson@DAMTP.cam.ac.uk
    """

# Load modules:
import numpy as np
from itertools import combinations_with_replacement

def legendre_array(X,lmax):
    """
        Calculates an array of Legendre polynomials
        with size: len(X) by lmax
        
        Parameters
        ----------
        lmax: int
        the maximum degree, must be positive
        X: array(float)
        points to calculate the polynomials on
        
        Returns
        ----------
        array(float)
        A table of the Legendre polynomials
        """
    
    # Initilise the array
    P = np.zeros((lmax,len(X)), dtype='float')
    
    # Set P_0 and P_l
    P[0,:]=1.0
    P[1,:]=X
    
    # Calculate the rest via iteration
    for n in range(2,lmax):
        P[n,:] = ((2*n-1)*X*P[n-1,:] - (n-1)*P[n-2,:])/n
    
    # return the array of Legendre polynomials
    return P

# Set maximums for l and i.
lmax = 50
imax = 5

# Compute number of points requiredfor the Gauss-Legendre
# quadtiture to be exact for a given lmax.
npts = 3*lmax//2+1

# Calculate Gauss-Legendre quadriture points, X, and weights, W.
X, W = np.polynomial.legendre.leggauss(npts)

# Create arrays for Legenre polynomials
P = legendre_array(X,lmax)


# Create Chebyshev Polynomials
# This could be changed to accept a general function or read from disk
# in future versions
L = np.linspace(-1,1,lmax)
C = legendre_array(L,imax)

# Compute the sum over L using a matrix product
Y = np.dot(C,P)

# Construct an iterator over possible triples of i
comb = combinations_with_replacement(range(imax),3)

# Calculate the integral (just a sum here) for each triple and print
# the result

# *******************************************************************
# *******************************************************************
# *****         Edit below here to parallelise the for          *****
# *******************************************************************
# *******************************************************************

for i,j,k in comb:
    z = np.sum(W[:]*Y[i,:]*Y[j,:]*Y[k,:])
    print("({},{},{}) produces {:5g}".format(i,j,k,z))

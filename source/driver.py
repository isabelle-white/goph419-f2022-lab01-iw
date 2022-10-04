"""
Created on Tue Sep 20 10:29:35 2022

This script contains a function to calculate the arcsin function of a real-value input

Inputs
------
Ea: approximate relative error
Es: stopping criteria, number of significant figures
n: iteration counter
fn: sum of the function so far
change_fn: last term to be calculated so far
fact_n: factorial value of n 
fact_2n: factorial value of 2n
    
Parameters
----------
x: float 
The argument of the arcsin function 

Returns
-------
float
The value of the arcsin function  

@author: izzywhite
"""


def arcsin(x):
    
    #import modules needed
    import numpy as np
    
    #define input parameters
    Ea = 1
    Es = 0.5*(10**-5)
    n = 1
    fn = 0
    fact_n = 1
    fact_2n = 2
    
    #set while statement for a stopping criteria (number of significant digits)
    while Ea > Es:
        #calculate the next term in the sqequence
        change_fn = ((2*x)**(2*n))/((n**2)*(fact_2n/((fact_n)**2)))
        #update the sum of the sequence
        fn += change_fn
        #update iteration counter and factorials to include pervious term
        n += 1
        fact_n *= n
        fact_2n *= (2*n)*(2*n-1)
        #calculate the approximate relative error
        Ea = abs(change_fn/fn)
    #calcualte the final sum for arcsin squared
    result = 0.5*fn
    #return arcsin
    return np.sqrt(result)
"""
Created on Mon Sep 19 14:02:00 2022

This script contains the function for the launch angle from the ratio of the escape velocity
and the maximum initial velocity, as well as alpha. This script calls the function arcsin 
from the module arcsin. 

Iputs
-----
    alpha = maximum alititude as a fraction of the Earth's radius
    ve_v0 = ratio of ve and v0
Parameters
----------
    v0 = maximum initial veolcity 
    ve_v0 = ratio of ve and v0
    
Output
------
    sin_launch_angle = sin of the launch angle
    launch_angle = lauch angle from the above parameters, this is in radians 


@author: izzywhite
"""

#defining parameters:

alpha = 0.25
ve_v0 = 2

def launch_angle(ve_v0, alpha):
    
    import numpy as np
    
    sin_launch_angle = (1+alpha)*np.sqrt(1 - (alpha/(1+alpha))*(ve_v0)**2)
    
    from arcsin import arcsin
    
    y = arcsin(sin_launch_angle)
        
    return y

a = launch_angle(ve_v0, alpha)

print ('Launch angle = ', a)
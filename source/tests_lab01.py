"""
Created on Wed Sep 21 17:25:08 2022

This script tests the output of launch_angle_range when given extreem values or 
value which don't make sense. 

Here I have edited the original launch_angle script so sensible errors are raised 
when common errors occur.

Input
-----
    alpha = maximum alititude as a fraction of the Earth's radius
    ve_v0 = ratio of ve and v0
    
Parameters
----------
    alpha = maximum alititude as a fraction of the Earth's radius
    ve = escape velocity 
    v0 = maximum initial veolcity 
    ve_v0 = ratio of ve and v0
    
Output
-------
    sin_launch_angle = sin of the launch angle
    launch_angle = lauch angle from the above parameters, this is in radians '

@author: izzywhite
"""

import numpy as np

#defining parameters:

alpha = 0.2
ve_v0 = 2


def tests(ve_v0, alpha):
    from launch_angle import launch_angle

    x= 1 - (alpha/(1+alpha))*(ve_v0)**2
    
    #test if the square root < 0
    if (x) < 0 :
        print('Test fail, the value under the squareroot = ', (x), '. This should be >0')
    else:
        print(f"Test passed for alpha={alpha} and ve_v0={ve_v0}.")
    #test if sin > 1 
        if (1+alpha)*np.sqrt(x) > 1:
            print('Test failed, calculated sin value = ', (1+alpha)*np.sqrt(x), '. It should be <1')
        else:
            print(f"Test passed for alpha={alpha} and ve_v0={ve_v0}.")   
    #test if part of the equation is 0
            if (x) == 0:   
                print('Test failed, launch angle  = 0' )
            else:
                print(f"Test passed for alpha={alpha} and ve_v0={ve_v0}.")
            
    #test if part of the equation is 0    
                if  (1+alpha) ==0:
                    print('Test failed, launch angle = 0')
                else:
                    print(f"Test passed for alpha={alpha} and ve_v0={ve_v0}.")    
    
    #if pass all the above tests calculate the launch angle using function launch_angle
    y = launch_angle(ve_v0, alpha)
        
    return y

angle = tests(ve_v0, alpha)
print ('Launch angle = ', angle)
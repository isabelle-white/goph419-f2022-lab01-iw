"""
Created on Mon Sep 19 14:46:53 2022

This script is for a function which calculates the acceptable launch angle range for 
a specific target amplitude (aplha). This function calls the function launch_angle from the 
module launch_angle.

Parameters
----------
    alpha = maximum alititude as a fraction of the Earth's radius
    ve = escape velocity 
    v0 = maximum initial veolcity 
    ve_v0 = ratio of ve and v0
    tol_alpha = tolerance for amplitude 
    
    min_altitude = minimum altitude including tolerance
    max_altitude = maximum altitude including tolerance 
    min_angle = minimum launch angle for the calculated maximum altitude
    max_angle = maximum launch angle for the calculated minimum altitude
    launch_range = array to store minimum and maximum launch angles, this is in radians 
    
Outputs
-------
    launch_range = array to store minimum and maximum launch angles
    

@author: izzywhite
"""

alpha = 0.25
ve_v0 = 2
tol_alpha = 0.02


def launch_angle_range(alpha, ve_v0, tol_alpha):

    #import the function tests to check the launch angle range each variables are changed
    from tests_lab01 import tests
    y = tests(ve_v0, alpha)  

    #create an empty array for the minimum and maximum launch angles
    launch_range = []
    
    #define the maximum and minimum altitudes acceptable 
    max_altitude = (1 + tol_alpha) * alpha 
    min_altitude = (1-tol_alpha) * alpha
    
    #call the function launch_angle
    from launch_angle import launch_angle
    
    #calculate the minimum launch angle for the max allowable altitude
    min_angle = launch_angle(ve_v0, max_altitude)
    #add this to the angle_range array
    launch_range.append(min_angle)
    
    #calculate the maximum launch angle for the min allowable altitude
    max_angle = launch_angle(ve_v0, min_altitude)
    #add this to the angle_range array
    launch_range.append(max_angle)
    
    return launch_range

angle_range = launch_angle_range(0.25, 2, 0.02)
print(f"Hand calculated launch angle range = 0.57409-0.61186 and launch_angle_range ={angle_range}.")
print ("Range of acceptable launch angles = ", angle_range)
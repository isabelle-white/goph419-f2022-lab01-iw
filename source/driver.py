"""Driver script for Assignment #1."""

def main():
	"""
	Created on Wed Sep 21 17:45:48 2022

	This script contains code to calculate the launch angle range and then plot graphs of launch angle against multiple different input values of alpha 
using the function launch_angle_range 

Inputs
------
    tol_alpha = tolerance for amplitude 
    ve_v0 = ratio of ve and v0
    alpha_range = range of input alpha values that give real results
    
Paramaters
----------
    tol_alpha = tolerance for amplitude 
    ve_v0 = ratio of ve and v0

Output
------
Graph of Minimum and Maximum launch angle against alpha


@author: izzywhite
"""

	import matplotlib.pyplot as plt
	import numpy as np
	from launch_angle_range import launch_angle_range


	figure, axis = plt.subplots(2, figsize=(10,10))

#keeping ve_v0 and tol_alpha constant
	ve_v0_set = 2
	tol_alpha = 0.04

#set empty arrays for the list of minimum and maximum values calculated
	minimum_angle_alpha =[]
	maximum_angle_alpha =[]

#set the range of acceptable alphas calculated from setting the boundary conditions and rearanging sin(phi) function
	alpha_range = np.arange(0, 0.333, 0.05)

#loop through all alphas in range to caluclate minimum and maximum angle for each within the set tolerance
	for i in alpha_range:
		y = launch_angle_range(i, ve_v0_set, tol_alpha)
		maximum_angle_alpha.append(y[1])
		minimum_angle_alpha.append(y[0])
    
	print('Minimum angles: ', minimum_angle_alpha)
	print('Maximum angles: ', maximum_angle_alpha)

#plot the values of launch angle against alpha. Adding labels and legend. 
	axis[0].plot(alpha_range, minimum_angle_alpha, label='Minimum Launch Angle')
	axis[0].plot(alpha_range, maximum_angle_alpha, label='Maximum Launch Angle')
	axis[0].set_xlabel("Alpha")
	axis[0].set_ylabel("Launch Angle")
	axis[0].set_title("Minimum and Maximum Launch Angle against Alpha")
	axis[0].legend()

#keeping alpha and tol_alpha constant
	alpha_set = 0.25

#set empty arrays for the list of minimum and maximum values calculated
	minimum_angle_ve_v0 =[]
	maximum_angle_ve_v0 =[]

#set the range of acceptable ve/v0 ratios calculated from setting the boundary conditions and rearanging sin(phi) function
	ve_v0_range = np.arange(1.342, 2.236, 0.025)

#loop through all ve_v0 in range to caluclate minimum and maximum angle for each within the set tolerance
	for i in ve_v0_range:
		y = launch_angle_range(alpha_set, i, tol_alpha)
		maximum_angle_ve_v0.append(y[1])
		minimum_angle_ve_v0.append(y[0])
    
	print('Minimum angles: ', minimum_angle_ve_v0)
	print('Maximum angles: ', maximum_angle_ve_v0)

#plot the values of the launch angles against ve_v0 values. Adding labels and legend. 
	axis[1].plot(ve_v0_range, minimum_angle_ve_v0, label='Minimum Launch Angle')
	axis[1].plot(ve_v0_range, maximum_angle_ve_v0, label='Maximum Launch Angle')
	axis[1].set_xlabel("Ve/Vo")
	axis[1].set_ylabel("Launch Angle")
	axis[1].set_title("Minimum and Maximum Launch Angle against Ve/V0")
	axis[1].legend()  

	plt.savefig('Graphs of Launch Angle against Alpha and Ve_V0')

if __name__ == "__main__":
        main()

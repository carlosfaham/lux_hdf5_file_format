import matplotlib.pyplot as plt
from scipy import interpolate
import matplotlib
import scipy as sp
import numpy as np

def plot_pmt_array(ax=None):
	
	# Shortcut for circle-drawing routine
	Circle = matplotlib.patches.Circle

	# Get the Top array PMT positions
	pmt_pos = get_top_pmt_pos_map()
	r_cm = 5.7/2*1.1

	# Open figure
	if not ax:
		fig = plt.figure(123)
		fig.clf()
		ax = fig.add_subplot(111)

	# Plot it
	ii = 0
	for xy in pmt_pos:
		# Need to use add_path to draw the circle
		ax.add_patch(Circle((xy[0]*1.1,xy[1]*1.1),r_cm,facecolor=(1,1,1),alpha=0.3))
		ii += 1

	ax.set_xlim([-30,30])
	ax.axis('equal')

def get_top_pmt_pos_map():
	# Got this from Matlab's LUXHitPattern
	pmt_pos = [[-12.0, 20.78],
			 [-15.0, 15.59],
			 [-18.0, 10.39],
			 [-21.0, 5.2],
			 [-9.0, 15.59],
			 [-12.0, 10.39],
			 [-15.0, 5.2],
			 [-6.0, 10.39],
			 [-9.0, 5.2],
			 [-3.0, 5.2],
			 [-24.0, 0.0],
			 [-21.0, -5.2],
			 [-18.0, -10.39],
			 [-15.0, -15.59],
			 [-18.0, 0.0],
			 [-15.0, -5.2],
			 [-12.0, -10.39],
			 [-12.0, 0.0],
			 [-9.0, -5.2],
			 [-6.0, 0.0],
			 [-12.0, -20.78],
			 [-6.0, -20.78],
			 [0.0, -20.78],
			 [6.0, -20.78],
			 [-9.0, -15.59],
			 [-3.0, -15.59],
			 [3.0, -15.59],
			 [-6.0, -10.39],
			 [0.0, -10.39],
			 [-3.0, -5.2],
			 [12.0, -20.78],
			 [15.0, -15.59],
			 [18.0, -10.39],
			 [21.0, -5.2],
			 [9.0, -15.59],
			 [12.0, -10.39],
			 [15.0, -5.2],
			 [6.0, -10.39],
			 [9.0, -5.2],
			 [3.0, -5.2],
			 [24.0, 0.0],
			 [21.0, 5.2],
			 [18.0, 10.39],
			 [15.0, 15.59],
			 [18.0, 0.0],
			 [15.0, 5.2],
			 [12.0, 10.39],
			 [12.0, 0.0],
			 [9.0, 5.2],
			 [6.0, 0.0],
			 [12.0, 20.78],
			 [6.0, 20.78],
			 [0.0, 20.78],
			 [-6.0, 20.78],
			 [9.0, 15.59],
			 [3.0, 15.59],
			 [-3.0, 15.59],
			 [6.0, 10.39],
			 [0.0, 10.39],
			 [3.0, 5.2],
			 [0.0, 0.0]]
 	return pmt_pos
 	
import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd

# Extracts data and places into list indexed by neutron
df = pd.read_excel('MCRD.xlsx', header = None)
df.values.T
N = []
for n in df.values.T:
    n = [eval(i) for i in n if type(i) is str]
    N.append(n)


# Sets up initial boundaries
fig, ax = plt.subplots()
b_lim, t_lim = -2, 10
plt.xlim(b_lim, t_lim)
plt.ylim(b_lim, t_lim)
plt.plot([0, 8, 8, 0, 0], [0, 0, 8, 8, 0], 'b-')
plt.grid()
tail_length = 3

def in_bounds(x, y):
	return True if (x > 0 and x < 8) and (y > 0 and y < 8) else False

# Function for updating the animation every timestep
def update(i):
	# clears the previous frame and redraws relevant info
	title = "NNY" + str(i)
	ax.cla()
	plt.xlim(b_lim, t_lim)
	plt.ylim(b_lim, t_lim)
	plt.grid()
	plt.plot([0, 8, 8, 0, 0], [0, 0, 8, 8, 0], 'b-')
	

	# progresses paths of each neutron
	for neut in N:
		x = [p[0] for p in neut if p is not None]
		y = [p[1] for p in neut if p is not None]

		if i < len(x):
			if i > 0 and i <= tail_length:
				ax.plot(x[:i+1], y[:i+1], 'r--')
			elif i > 0:
				ax.plot(x[i-tail_length:i+1], y[i-tail_length:i+1], 'r--')
			ax.plot(x[i], y[i], 'rD')
		elif i >= len(x):
			if in_bounds(x[-1], y[-1]):
				ax.plot(x[-1], y[-1], 'gD')
			else:
				ax.plot(x[-1], y[-1], 'bD')
	plt.savefig(title, dpi='figure')

ani = animation.FuncAnimation(fig, update, frames=max([len(i) for i in N]), interval=200)
plt.show()











	# def update(i):
	# 	ax.cla()
	# 	plt.xlim(-x_lim, x_lim)
	# 	plt.ylim(-y_lim, y_lim)
	# 	plt.grid()

	# 	if i > 0 and i <= tail_length:
	# 		ax.plot(x[:i+1], y[:i+1], 'r')
	# 	elif i > 0:
	# 		ax.plot(x[i-tail_length:i+1], y[i-tail_length:i+1], 'r')
	# 	return ax.plot(x[i], y[i], 'ro')

	# ani = animation.FuncAnimation(fig, update, frames=len(x), interval=200)
	# plt.show()

# def manhattandist(x1, x2, y1, y2):
# 	return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


# def getSlope(lx, rx, dy, uy):

# 	return (rx - lx) / (uy - dy)

# def plhelper(fluxdist, l1, l2):

# 	x1, y1 = l1
# 	x2, y2 = l2

# 	lx = min(x1, x2)
# 	rx = max(x1, x2)
# 	dy = min(y1, y2)
# 	uy = max(y1, y2)

# 	m = getSlope(lx, rx, dy, uy)


	

# def pathLengthSummer(matrix):

# 	fluxdist = np.zeros((8, 8))

# 	for nLifetime in matrix:
# 		prevLoc = None
# 		for loc in nLifetime:
# 			if loc is None:
# 				break
# 			if prevLoc is not None:
# 				plhelper(fluxdist, prevLoc, loc)
# 			prevLoc = loc

# 	return fluxdist












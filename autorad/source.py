import numpy as np
import matplotlib.pyplot as plt

class Source(object):
	def __init__(self, World, strength, x, y):
		self.world = World
		self.strength = float(strength)
		self.x = x
		self.y = y

	def plot(self):
		plt.scatter(self.x, self.y, marker="x", color='k', label='Source')

	def cast_ray(self, x, y):
		x0, y0 = self.x, self.y
		ix0, iy0 = x0, y0
		unocc, occ = 0, 0

		while (x-x0)*(y-y0):

			dx = x - x0
			dy = y - y0
			dnorm = np.sqrt(dx**2 + dy**2)
			dx /= dnorm
			dy /= dnorm
			dx_nextedge = 1 if dx>0 else 0
			dy_nextedge = 1 if dy>0 else 0

			rx = np.abs((self.world.x_edges[ix0 + dx_nextedge] - x0) / dx)
			ry = np.abs((self.world.y_edges[iy0 + dy_nextedge] - y0) / dy)

			re = np.sqrt((x0-x)**2 + (y0-y)**2)
			r = np.array([rx, ry, re]).min()

			if self.world.occlusion_mask[ix0,iy0]:
				occ += r
			else:
				unocc += r

			if (r - rx < 1e-5):
				ix0 += 2*dx_nextedge - 1
			if (r - ry < 1e-5):
				iy0 += 2*dy_nextedge - 1

			x0 += (dx * r)
			y0 += (dy * r)

		return unocc, occ


	def compute_flux(self, x, y):
		r2 = (self.x - x)**2. + (self.y - y)**2.

		unocc, occ = self.cast_ray(x,y)
		atten = np.exp(-self.world.occlusion_mu * occ)

		return self.strength * atten / (r2 + 1e-10)

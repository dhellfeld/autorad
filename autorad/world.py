import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

class World(object):
	def __init__(self, nx, ny, bkgrate):
		self.nx, self.ny = nx, ny
		self.x, self.y = np.meshgrid(range(nx), range(ny))
		self.x_edges = np.arange(nx+1)-0.5
		self.y_edges = np.arange(ny+1)-0.5

		self.bkgrate = bkgrate

		self.occlusion_mask = np.zeros((nx,ny))
		self.occlusion_mu = 0.

		self.measurements_sum = np.zeros((nx, ny))
		self.measurements_num = np.zeros((nx, ny))
		self.measurements_mean = np.zeros((nx, ny))

	def isin(self, x, y):
		if (x <= self.x.max()) and (x >= self.x.min()) and \
		   (y <= self.y.max()) and (y >= self.y.min()):
			return True
		else:
			return False

	def plot_measurements(self, selection="mean"):
		if selection == "mean":
			f = self.measurements_mean.T
			norm=LogNorm()
		elif selection == "sum":
			f = self.measurements_sum.T
			norm=LogNorm()
		elif selection == "num":
			f = self.measurements_num.T
			norm=None
		else:
			raise Exception()

		im = plt.imshow(f,
						interpolation='nearest',
						aspect='equal',
						origin='lower',
						cmap='Greens',
						norm=norm)
		plt.colorbar(im)

		plt.imshow(np.ma.masked_where(self.occlusion_mask == 0, self.occlusion_mask).T,
					interpolation='nearest',
					origin='lower',
					aspect='equal',
					cmap="Greys_r")

		plt.xlim(self.x.min(), self.x.max())
		plt.ylim(self.y.min(), self.y.max())
		plt.xlabel("X")
		plt.ylabel("Y")

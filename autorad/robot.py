import numpy as np
import matplotlib.pyplot as plt

class Robot(object):
	def __init__(self, World, x, y, mt):
		self.world = World
		self.x = x
		self.y = y
		self.xs = [self.x]
		self.ys = [self.y]
		self.movements = ['here', 'left', 'right', 'up', 'down']
		self.measurement_time = mt
		self.measurements = []

	def append_position(self):
		self.xs.append(self.x)
		self.ys.append(self.y)

	def can_move(self, x, y):
		if self.world.isin(x, y):
			if not self.world.occlusion_mask[x, y]:
				return True
		return False

	def _move_right(self):
		if self.can_move(self.x+1, self.y):
			self.x = self.x+1
		self.append_position()

	def _move_left(self):
		if self.can_move(self.x-1, self.y):
			self.x = self.x-1
		self.append_position()

	def _move_up(self):
		if self.can_move(self.x, self.y+1):
			self.y = self.y+1
		self.append_position()

	def _move_down(self):
		if self.can_move(self.x, self.y-1):
			self.y = self.y-1
		self.append_position()

	def move(self, where):
		if where == "right":
			self._move_right()
		elif where == "left":
			self._move_left()
		elif where == "up":
			self._move_up()
		elif where == "down":
			self._move_down()
		else:
			raise Exception()

	def measure(self, source, where='here'):
		xt, yt = self.x, self.y
		if where == 'right':
			if self.can_move(self.x+1, self.y):
				xt, yt = self.x+1, self.y
		elif where == 'left':
			if self.can_move(self.x-1, self.y):
				xt, yt = self.x-1, self.y
		elif where == 'up':
			if self.can_move(self.x, self.y+1):
				xt, yt = self.x, self.y+1
		elif where == 'down':
			if self.can_move(self.x, self.y-1):
				xt, yt = self.x, self.y-1
		elif where == 'here':
			pass
		else:
			raise Exception()

		sval = np.random.poisson(source.compute_flux(xt, yt) * self.measurement_time)
		bval = np.random.poisson(self.world.bkgrate * self.measurement_time)
		val = sval + bval
		self.measurements.append(val)

		self.world.measurements_sum[xt, yt] += val
		self.world.measurements_num[xt,yt] += 1
		self.world.measurements_mean[xt, yt] = val / self.world.measurements_num[xt, yt]

		return val / self.world.measurements_num[xt, yt]

	def measure_all(self, source):
		vals = []
		for w in self.movements:
			vals.append(self.measure(source, where=w))
		return vals

	def plot_current(self):
		plt.scatter(self.x, self.y, marker="o", color='r')

	def plot_starting(self):
		plt.scatter(self.xs[0], self.ys[0], marker="o", color='g')

	def plot_trajectory(self):
		plt.scatter(self.xs[0], self.ys[0], marker="o", color='g', alpha=0.6, label='Start')
		plt.scatter(self.x, self.y, marker="o", color='r', alpha=0.6, label='Finish')
		plt.plot(self.xs, self.ys, color='b', linewidth=0.5, alpha=0.6, label='Path')

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LogNorm
import numpy as np


def plot_results_map(robot, source):

	plt.figure(figsize=(9,4))

	# World with measured values
	plt.subplot(121)
	robot.world.plot_measurements(selection="mean")
	robot.plot_trajectory()
	source.plot()
	plt.legend(loc=2)
	plt.title("Mean measurements")

	# World with position tracking
	plt.subplot(122)
	robot.world.plot_measurements(selection="num")
	robot.plot_trajectory()
	source.plot()
	plt.legend(loc=2)
	plt.title("Number of measurements")
	plt.tight_layout()
	plt.show()


def plot_results_measurements(robot):

	plt.figure(figsize=(9,4))
	plt.semilogy(robot.measurements[0::5])
	plt.ylim(0.1)
	plt.xlabel("Measurement number")
	plt.ylabel("Measurement value")
	plt.tight_layout()
	plt.show()


def animate_results(robot, source):

	fig, axs = plt.subplots(2, 1, figsize=(7,7))
	axs[1].set_yscale('log')
	axs[1].set_xlim(0, len(robot.xs))
	axs[1].set_ylim(1e-1, np.max(robot.measurements[0::5])*1.1)

	## World
	axs[0].imshow(np.ma.masked_where(robot.world.occlusion_mask == 0, robot.world.occlusion_mask).T,
					interpolation='nearest',
					origin='lower',
					aspect='equal',
					cmap="Greys_r")

	axs[0].set_xlabel("X (m)")
	axs[0].set_ylabel("Y (m)")
	axs[1].set_xlabel("Measurement number")
	axs[1].set_ylabel("Measurement value")

	## Source
	axs[0].scatter(source.x, source.y, marker="x", color='k', label='Source')

	## Starting/ending robot
	axs[0].scatter(robot.xs[0], robot.ys[0], marker="o", color='g', alpha=0.6, label='Start')
	axs[0].scatter(robot.xs[-1], robot.ys[-1], marker="o", color='r', alpha=0.6, label='Finish')

	## Initialize trajectory
	line1, = axs[0].plot([], [], lw=1, label="Path")
	line2, = axs[1].plot([], [], lw=1.5, c='k')
	line = [line1, line2]
	xdata, ydata, mdata, ii = [], [], [], []

	## Animate
	def init():
		for l in line:
			l.set_data([], [])
		return line
	def animate(i):
		xdata.append(robot.xs[i])
		ydata.append(robot.ys[i])
		mdata.append(robot.measurements[0::5][i])
		ii.append(i)

		line[0].set_data(xdata, ydata)
		line[1].set_data(ii, mdata)
		return line
	anim = FuncAnimation(fig, animate, frames=len(robot.xs), interval=2, blit=True, repeat=False)

	## Render
	axs[0].legend(loc=2)
	plt.tight_layout()
	plt.show()

import numpy as np

def gradient_search(robot, source, max_steps=None):

	# Set max_steps to size of grid if none provided
	max_steps = robot.world.nx*robot.world.ny if max_steps is None else max_steps
	for i in range(max_steps):

		# Measure in all directions, compute gradient to current position
		vals = robot.measure_all(source)
		grad = vals[1:] / (vals[0] + 1e-10)

		# Descending order of gradients
		ordered_grad = list(reversed(np.argsort(grad)))

		# Move in direction of largest gradient
		next_move = robot.movements[1:][ordered_grad[0]]
		robot.move(next_move)

		# If source is found, stop
		if (robot.x, robot.y) == (source.x, source.y):
			print(f"Found source after {i} steps ({i*robot.measurement_time:.2f} s)")
			return robot

	print(f"Didn't find source, but reached max_steps ({max_steps}).")
	return robot

########################################################################
# # TODO:
# More robust decision algorithms
#    - probabalistic gradient search?
#    - gradient annealing?
#    - deep reinforcement learning
# Incorporate Poisson likelihood into search
#
#

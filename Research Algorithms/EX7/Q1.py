import matplotlib.pyplot as plt
import numpy as np
import cvxpy as cp
import time as time


def cvxpy(mat, vec):
    # Here we will solve with cvxpy
    start_time = time.time()  # Start the time
    x = cp.Variable(mat.shape[0])
    cost = cp.sum_squares(mat @ x - vec)  # The sum of the squares of the entries
    prob = cp.Problem(cp.Minimize(cost))
    prob.solve()  # Compiles and solves the problem using the specified method
    end_time = time.time()  # End the time
    return end_time - start_time  # Return the time the solving took


def numpy(mat, vec):
    # Here we will solve with numpy
    start_time = time.time()  # Start the time
    np.linalg.lstsq(mat, vec, rcond=None)  # Return the least-squares solution to a linear matrix equation
    end_time = time.time()  # End the time
    return end_time - start_time  # Return the time the solving took


def draw(size, numpy_time, cvxpy_time):
    plt.plot(size, numpy_time, label='numpy')
    plt.plot(size, cvxpy_time, label='cvxpy')
    plt.ylabel('time')
    plt.xlabel('size')
    plt.legend()
    plt.show()


def Start():
    size, np_times, cp_times = [], [], []
    for s in range(10, 100):
        mat, vec = np.random.rand(s, s), np.random.rand(s)
        size.append(s)
        np_time = numpy(mat, vec)
        np_times.append(np_time)
        cp_time = cvxpy(mat, vec)
        cp_times.append(cp_time)
    # Drawing the Graph
    draw(size, np_times, cp_times)


if __name__ == '__main__':
    Start()

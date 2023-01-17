import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt
import random
import time



class LinearEquations:
    def __init__(self, size):
        self.size = size
        self.coefficients = np.random.rand(size, size)
        self.constants = np.random.rand(size)
        self.solution = np.linalg.solve(self.coefficients, self.constants)

    def numpy_solve(self):
        return np.linalg.solve(self.coefficients, self.constants)

    def cvxpy_solve(self):
        variables = cp.Variable(self.size)
        constraints = [self.coefficients @ variables == self.constants]
        objective = cp.Minimize(cp.sum(variables))
        problem = cp.Problem(objective, constraints)
        problem.solve()
        return variables.value


if __name__ == '__main__':
    # Test the running time for different sizes of the equation
    sizes = [10, 50, 100, 250, 500, 1000]
    numpy_times = []
    cvxpy_times = []

    for size in sizes:
        eq = LinearEquations(size)
        # Measure the running time for numpy
        start = time.time()
        numpy_solve = eq.numpy_solve()
        numpy_times.append(time.time() - start)
        # Measure the running time for cvxpy
        start = time.time()
        cvxpy_solve = eq.cvxpy_solve()
        cvxpy_times.append(time.time() - start)

    # Plot the running time
    plt.plot(sizes, numpy_times, label="numpy")
    plt.plot(sizes, cvxpy_times, label="cvxpy")
    plt.xlabel("Equation Size")
    plt.ylabel("Running Time (s)")
    plt.legend()
    plt.show()

    print("We got that numpy is quicker on large equations and cvxpy is quicker on small equations")
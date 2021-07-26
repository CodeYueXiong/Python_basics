import numpy as np

# Solving following systems of linear equations, using numpy
# 1a + 1b = 35
# 2a + 4b = 94

a = np.array([[1, 1], [2, 4]])
b = np.array([35, 94])

print(np.linalg.solve(a,b))
# What is Interpolation?
# Interpolation is a method for generating points between given points.
# For example: for points 1 and 2, we may interpolate and find points 1.33 and 1.66.
# Interpolation has many usage, in Machine Learning we often deal with missing data in a dataset, interpolation is often used to substitute those values.
# This method of filling values is called imputation.
# Apart from imputation, interpolation is often used where we need to smooth the discrete points in a dataset.
# How to Implement it in SciPy?
# SciPy provides us with a module called scipy.interpolate which has many functions to deal with interpolation:
# 1D Interpolation
# The function interp1d() is used to interpolate a distribution with 1 variable.
# It takes x and y points and returns a callable function that can be called with new x and returns corresponding y.
#For given xs and ys interpolate values from 2.1, 2.2... to 2.9:
from scipy.interpolate import interp1d
import numpy as np
xs = np.arange(10)
ys = 2*xs + 1
interp_func = interp1d(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)

# Spline Interpolation
# In 1D interpolation the points are fitted for a single curve whereas in Spline interpolation the points
# are fitted against a piecewise function defined with polynomials called splines.
# The UnivariateSpline() function takes xs and ys and produce a callable funciton that can be called with new xs.
# Piecewise function: A function that has different definition for different ranges.
# Find univariate spline interpolation for 2.1, 2.2... 2.9 for the following non linear points:
from scipy.interpolate import UnivariateSpline
import numpy as np
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1
interp_func = UnivariateSpline(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)

# Interpolation with Radial Basis Function
# Radial basis function is a function that is defined corresponding to a fixed reference point.
# The Rbf() function also takes xs and ys as arguments and produces a callable function that can be called with new xs.
# Interpolate following xs and ys using rbf and find values for 2.1, 2.2 ... 2.9:

from scipy.interpolate import Rbf
import numpy as np
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1
interp_func = Rbf(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)
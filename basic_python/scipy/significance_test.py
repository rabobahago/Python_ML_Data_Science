# What is Statistical Significance Test?
# In statistics, statistical significance means that the result that was produced has a reason behind it, it was not produced randomly, or by chance.

# SciPy provides us with a module called scipy.stats, which has functions for performing statistical significance tests.

# Here are some techniques and keywords that are important when performing such tests:

# Hypothesis in Statistics
# Hypothesis is an assumption about a parameter in population.
# Null Hypothesis
# It assumes that the observation is not statistically significant.
# Alternate Hypothesis
# It assumes that the observations are due to some reason.
# It's alternate to Null Hypothesis.
# For an assessment of a student we would take:
# "student is worse than average" - as a null hypothesis, and:
# "student is better than average" - as an alternate hypothesis.
# One tailed test
# When our hypothesis is testing for one side of the value only, it is called "one tailed test".

# For the null hypothesis:
# "the mean is equal to k", we can have alternate hypothesis:
# "the mean is less than k", or:
# "the mean is greater than k"

# Two tailed test
# When our hypothesis is testing for both side of the values.
# For the null hypothesis:
# "the mean is equal to k", we can have alternate hypothesis:
# "the mean is not equal to k"
# In this case the mean is less than, or greater than k, and both sides are to be checked.

# P value
# P value tells how close to extreme the data actually is.
# P value and alpha values are compared to establish the statistical significance.
# If p value <= alpha we reject the null hypothesis and say that the data is
# statistically significant. otherwise we accept the null hypothesis.

# T-Test
# T-tests are used to determine if there is significant deference between means of two variables
# and lets us know if they belong to the same distribution.
# It is a two tailed test.
# The function ttest_ind() takes two samples of same size and produces a tuple of t-statistic and p-value.
# Find if the given values v1 and v2 are from same distribution:
import numpy as np
from scipy.stats import ttest_ind
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1, v2)
print(res)

# KS-Test
# KS test is used to check if given values follow a distribution.
# The function takes the value to be tested, and the CDF as two parameters.
# A CDF can be either a string or a callable function that returns the probability.
# It can be used as a one tailed or two tailed test.
# By default it is two tailed. We can pass parameter alternative as a string of one of two-sided, less, or greater.
# Find if the given value follows the normal distribution:

import numpy as np
from scipy.stats import kstest
v = np.random.normal(size=100)
res = kstest(v, 'norm')
print(res)
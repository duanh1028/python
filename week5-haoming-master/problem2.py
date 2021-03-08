import math
import numpy as np
import scipy as sp
from scipy.stats import t
from scipy.stats import norm

# q1
data = [3, -3, 3, 12, 15, -16, 17, 19, 23, -24, 32]
size = len(data)

mean = np.mean(data)

std_error = np.std(data) / math.sqrt(size)
t_c = t.ppf(1 - (1 - 0.95) / 2, size - 1)
mu_upper = np.mean(data) + t_c * std_error
mu_lower = np.mean(data) - t_c * std_error

print("question1:")
print("The mean of the sample is %f." %(mean))
print("The standard error of the sample is %f." %(std_error))
print("The standard statistic (t value) is %f." %(t_c))
print("The interval is:")
print([mu_lower, mu_upper])

# q2
t_c = sp.stats.t.ppf(1 - (1 - 0.9) / 2, size - 1)
mu_upper = np.mean(data) + t_c * std_error
mu_lower = np.mean(data) - t_c * std_error
print("question2:")
print("The standard statistic (t value) is %f." %(t_c))
print("The interval is:")
print([mu_lower, mu_upper])

# q3
z_c = sp.stats.norm.ppf(1 - 0.05 / 2)
mu_upper = mean + z_c * 16.836 / math.sqrt(size)
mu_lower = mean - z_c * 16.836 / math.sqrt(size)
std_error = 16.836 / (size ** 0.5)
print("question3:")
print("The standard statistic (z value) is %f." %(z_c))
print("The standard error of the sample is %f." %(std_error))
print("The interval is:")
print([mu_lower, mu_upper])

# q4
std_error = np.std(data) / math.sqrt(size)
t_c = mean / std_error
p4 = t.cdf(t_c, size - 1)
confi = 1 - 2 * (1 - p4)
print("question4:")
print("The confidence is: %f%%." %(confi))

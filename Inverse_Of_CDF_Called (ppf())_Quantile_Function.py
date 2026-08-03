# using the inverse CDF(called ppf()) in python...
# importing norm(normal) from scipy.stats
from scipy.stats import norm

# define formula for inverse of CDF is ppf()
x = norm.ppf(0.95, loc=64.43, scale=2.99)

# print value of x...
print(x)
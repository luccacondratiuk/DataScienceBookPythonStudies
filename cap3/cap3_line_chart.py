# Line Charts are a great way of showing tendencies

from matplotlib import pyplot as plt

variance = list(2**i for i in range(9))
bias_squared = list(2**i for i in range(9))
variance.sort()
bias_squared.sort(reverse=True)
total_error = [x+y for x,y in zip(variance,bias_squared)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label='Variance')          # Green Line, Labeled Variance
plt.plot(xs, bias_squared, 'r-', label='Bias²')         # Red Line, Labeled Bias²
plt.plot(xs, total_error, 'b:', label='Total Error')    # Blue Dash-Line, Labeled Total Error
plt.legend(loc=9)                                       # Loc=9 -> Top Center
plt.xlabel("Model Complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.show()


# Scatter Charts are a good way of showing correlation between data pairs

from matplotlib import pyplot as plt

# Is possible to visualize a linear correlation between number of friends,
# and time spent on a website
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(
        label,
        xy=(friend_count, minute_count),
        xytext=(5,-5),
        textcoords='offset points'
    )
plt.title("Daily Minutes vs. Nº of friends")
plt.xlabel("Nº of friends")
plt.ylabel("Daily minutes Spent on the website")
plt.show()


# Not possible to relate test 1 and 2 grades

grades_test1 = [99, 90, 85, 97, 80]
grades_test2 = [100, 85, 60, 90, 70]

plt.scatter(grades_test1, grades_test2)
plt.title("Test 1 vs Test 2 grades")
plt.xlabel("Test 1")
plt.ylabel("Test 2")
plt.show()


plt.scatter(grades_test1, grades_test2)
plt.title("Test 1 vs Test 2 grades")
plt.xlabel("Test 1")
plt.ylabel("Test 2")
plt.axis("equal")
plt.show()

# May be a good option for showing how quantities may vary in
# in a discrete set of items
# Example 1: Number of oscars for some movies:

from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5,11,3,8,10]

plt.bar(range(len(movies)),num_oscars)
plt.title("Movies")
plt.ylabel("Nº of Academy Awards")
plt.xticks(range(len(movies)), movies)
plt.show()


# Bar Chats are a good option for plotting numerical histograms
# and show the distribution of the values
# Example 2: Distribution of grades

from collections import Counter
import random
random.seed(10)
grades = random.sample(list(range(0,101)),20)                       # generate 20 random grades from 0 to 100 into a list
histogram = Counter(min(grade // 10 * 10,90) for grade in grades)   # Grouping grades in intervals
plt.bar(
    [x + 5 for x in histogram.keys()],                              # Moving bars to the right by 5
    histogram.values(),                                             # Values
    10,                                                             # Atribute column width
    edgecolor=(0,0,0)                                               # Putting an edge (black)
)
plt.axis([-5,105,0,10])                                             # X Axis from -5 to 105 and Y from 0 to 10
plt.xticks([10 * i for i in range(11)])                             # X ticks from 0 to 100 increment by ten
plt.xlabel("Grades")
plt.ylabel("Nº of students")
plt.title("Grade Distribution")
plt.show()

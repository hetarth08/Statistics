import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mode,norm

#Task 1: Generate 100 Random Numbers
np.random.seed(42)

data = np.random.normal(50, 10, 100)

mean = 50
std_dev = 10

x = np.linspace(20, 80, 100)
y = norm.pdf(x, loc=mean, scale=std_dev)

plt.hist(data, bins=15, density=True, edgecolor="black")
plt.plot(x, y)

plt.title("Normal Distribution")
plt.xlabel("Random Numbers")
plt.ylabel("Frequency")
plt.show()

#Task 2: Fitness Tracker Step Counts
step_counts=[
    6000,6500,7000,7500,7800,
    8000,8200,8400,8500,8500,
    8500,8600,8800,9000,9200,
    9500,9800,10000,10500,11000
]

step_mean=np.mean(step_counts)
step_median=np.median(step_counts)
step_mode=mode(step_counts,keepdims=False).mode

print("\nTask 2: Fitness Tracker")
print("Mean:",step_mean)
print("Median:",step_median)
print("Mode:",step_mode)

if abs(step_mean-step_median) < 500:
    print("Mean and median are approximately equal.")
else:
    print("Mean and median are not approximately equal.")

#Task 3: Online Game Scores
scores=np.random.normal(78,15,200)

count=0

for score in scores:
    if 55 <= score <= 85:
        count += 1

print("\nTask 3: Online Game Scores")
print("Total Players:",len(scores))
print("Players scoring between 55 and 85:",count)
print("Percentage:",round((count / 200)*100,2),"%")
print("Approximately 68% of players are expected in this range.")

# Task 4: Real-World Example
print("\nTask 4: Normal Distribution Example")

print("Song durations on Spotify can sometimes follow an")
print("approximately normal distribution within a similar music category.")
print("Most songs may have durations around the average, while")
print("very short and very long songs are less common.")

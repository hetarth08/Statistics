import random
import numpy as np
import matplotlib.pyplot as plt

#Task 1: Instagram Hours and Posts
instagram_hours=[1,2,2,3,3,4,5]
posts_per_day=[1,1,2,2,3,3,5]

plt.scatter(instagram_hours,posts_per_day)
plt.title("Instagram Usage and Posts")
plt.xlabel("Hours Spent on Instagram")
plt.ylabel("Number of Posts")
plt.show()

print("Task 1: The relationship shows a positive correlation")

#Task 2: Zomato and Swiggy Orders
zomato_orders=[2,4,3,6,5,7]
swiggy_orders=[3,5,4,7,6,8]

correlation=np.corrcoef(zomato_orders,swiggy_orders)

print("\Task 2: Correlation Coefficient")
print(correlation)
print("The correlation is positive.")

#Task 3: Daily Life Correlation
print("\nTask 3: Daily Life Example")

print("I expect a negative correlation between the number of")
print("Youtube videos watched and daily study hours.")
print("When I spend more time watching Youtube, I may have")
print("less time available for studying.")

#Task 4: Spotify Time and Test Marks
spotify_hours=[1,2,3,4,5,6,7,8,9,10]
test_marks=[95,90,85,80,75,70,65,60,55,50]

print("\nTask 4: Spotify and Test Marks")
print("Spotify Hours:",spotify_hours)
print("Test Marks:",test_marks)

correlation=np.corrcoef(spotify_hours,test_marks)
print("Correlation Coefficient:",correlation[0,1])

plt.scatter(spotify_hours,test_marks)
plt.title("Spotify Time and Test Marks")
plt.xlabel("Hours Spent on Spotify")
plt.ylabel("Test Marks")
plt.show()


print("The dataset shows a strong negative correlation")
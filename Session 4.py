import statistics
import matplotlib.pyplot as plt

#Task 1:Swiggy daily order counts
orders=[12,15,17,14,13,16,200,18,14,15]

print("Task 1:Daily Order Counts")
print("Order Data:",orders)
print("Distribution: Right Skewed")
print("Reason: The value 200 is much higher than the other values.")

plt.hist(orders, bins=10, edgecolor="black")
plt.title("Daily Swiggy Order Counts")
plt.xlabel("Number of Orders")
plt.ylabel("Number of Days")
plt.show()

#Task 2:Instagram followers counts
followers=[5,7,8,8,9,10,12,15,95]

mean_followers=statistics.mean(followers)
median_followers=statistics.median(followers)

print("\nTask 2:Instagram Followers")
print("Mean:",round(mean_followers,2))
print("Median:",median_followers)

print("Mean is higher than median.")
print("The data is right skewed because of the high value 95.")

#Task 3:Real-world example of right-skewed data
youtube_views=[100,150,200,250,300,500,10000]

print("\nTask 3:Youtube Videos Views")
print("Example:",youtube_views)
print("This data is right skewed because most videos have")
print("fewer views while a few videos have very high views.")

#Task 4:Flipkart product ratrings
ratings=[3,3,4,4,4,5,5,5,5,5]

rating_values=[3,4,5]
rating_counts=[ratings.count(i) for i in rating_values]

print("\nTask 4:Flipkart Product Ratings")
print("Ratings:",ratings)
print("Frequency:",rating_counts)
print("Distribution: Left Skewed")
print("Reason: Most ratings are 4 or 5, with fewer low ratings.")

plt.bar(rating_values, rating_counts, edgecolor="black")
plt.title("Flipkart Product Ratings")
plt.xlabel("Ratings")
plt.ylabel("Frequency")
plt.xticks(rating_values)
plt.show()
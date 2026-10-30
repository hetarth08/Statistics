import random

#Task 1: Probability of Getting Heads
def calculate_probability(event_count,total_outcomes):
    return event_count/total_outcomes

heads_probability=calculate_probability(1,2)

print("Task 1: Coin Toss")
print("Probability of getting Heads:",heads_probability)

#Task 2: Rolling a Dice 100 Times
count_six=0

for i in range(100):
    dice=random.randint(1,6)

    if dice==6:
        count_six +=1

experimental_probability=calculate_probability(count_six,100)

print("\nTask 2: Dice Rolling")
print("Number of times 6 appeared:",count_six)
print("Experimental Probability:",experimental_probability)

#Task 3: Probability of picking a pop song
genres=[
    "pop","rock","pop","hiphop","jazz",
    "pop","rock","pop","classical","hiphop",
    "pop","rock","jazz","pop","hiphop",
    "rock","pop","jazz","pop","rock"
]

pop_count=genres.count("pop")
pop_probability=calculate_probability(pop_count,len(genres))

print("\nTask 3: Spotify Songs")
print("Total Pop Songs:",pop_count)
print("Probability of picking a Pop song:",pop_probability)

#Task 4: Probability of Ordering Food and Desserts
def food_and_dessert_probability(food_users,dessert_users):
    food_set=set(food_users)
    dessert_set=set(dessert_users)

    both_users=food_set.intersection(dessert_set)
    all_users=food_set.union(dessert_set)

    if len(all_users)==0:
        return 0
    return len(both_users)/len(all_users)

zomato_users=[101,102,103,104,105,106]
dessert_users=[103,104,105,107,108]

result=food_and_dessert_probability(zomato_users,dessert_users)

print("\nTask 4: Food and Dessert")
print("Probability of ordering both:",result)

#Task 5: Conditional Probability in Flipkart
phone_buyers=100
headphone_buyers=40

probability=calculate_probability(headphone_buyers,phone_buyers)

print("\nTask 5: Flipkart Recommendations")
print("Probability of buying headphones given a phone purchase:",probability)

if probability > 0.3:
    print("Flipkart can recommmend headphones to phone buyer.")
else:
    print("Flipkart can show other product recommendations")
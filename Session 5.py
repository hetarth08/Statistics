#Task 1
print("Population: All Instagram followers of an account.")
print("Sample: 50 followers selected from that account.")

#Task 2
import random

user_ids=["user" + str(i) for i in range(1, 1001)]
sample_users=random.sample(user_ids, 50)

print("\nSelected 50 users:")
for user in sample_users:
    print(user)
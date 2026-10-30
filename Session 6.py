from scipy.stats import ttest_ind_from_stats

#Task 1:Hypothesis Testing
print("TASK 1: Hypotheses")

print("H0: People spend equal or less time on Instagram than Youtube.")
print("H1: People spend more time on Instagram than Youtube.")

#Task 2:Two-Sample T-test
print("\nTASK 2: Zomato A/B Test")

mean_a=350
mean_b=320
std_a=50
std_b=50
users_a=30
users_b=30

result=ttest_ind_from_stats(
    mean1=mean_a,
    std1=std_a,
    nobs1=users_a,
    mean2=mean_b,
    std2=std_b,
    nobs2=users_b
)

print("T-statistics:", round(result.statistic, 4))
print("P-value:",round(result.pvalue, 4))

if result.pvalue < 0.05:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")

#Task 3:Paytm A/B Testing
print("\nTASK 3: Paytm A/B Test")

print("Control Group: Old payment button.")
print("Variant Group: New payment button.")
print("Metric: Payment completion rate.")
print("H0: New button does not increase payment completion.")
print("H1: New button increases payment collection.")

#Task 4: Flipkart Wishlist Button
print("\nTASK 4: Flipkart Wishlist Button")

new_button_clicks=520
old_button_clicks=480

print("New button clicks:",new_button_clicks)
print("Old button clicks:",old_button_clicks)
print("Difference in clicks:",new_button_clicks-old_button_clicks)

print("A p-value is required to decide statistical significance.")
print("The number of users in each group is also required.")
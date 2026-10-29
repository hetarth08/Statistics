import statistics
import math

#Task 1:Calculate variance by hand
steps=[4500,7000,5000,8000,4000,9000,6000]

mean_steps=sum(steps)/len(steps)
print("Task 1:Variance of Daily Steps")
print("Mean =",round(mean_steps,2))

squared_deviations=[]

for step in steps:
    deviation=step-mean_steps
    squared=deviation**2
    squared_deviations.append(squared)
    print(step,"-",round(mean_steps,2),"-",round(deviation,2),
          "Squared =",round(squared,2))

variance=sum(squared_deviations)/len(squared_deviations)
print("Variance =",round(variance,2))

#Task 2:Calculate standard deviation of exam scores
def calculate_standard_deviation(scores):
    return round(statistics.pstdev(scores),2)

exam_scores=[75,80,85,90,70]
print("\nTask 2:Standard Deviation of Exam Scores")
print(calculate_standard_deviation(exam_scores))

#Task 3:Compare daily spending
friend_a=[200,200,200,200,200]
friend_b=[100,300,150,400,50]

sd_a=statistics.pstdev(friend_a)
sd_b=statistics.pstdev(friend_b)

print("\nTask 3: Daily Spending")
print("Friend A Standard Deviation:",round(sd_a,2))
print("Friend B Standard Deviation:",round(sd_b,2))
print("Friend A has more consistent spending because the")
print("standard deviation is zero")

#Task 4:Employee salary analysis
salaries=[28000,29000,27000,60000,26500,27500]

salary_variance=statistics.pvariance(salaries)
salary_sd=statistics.pstdev(salaries)

print("\nTask 4:Salary Analysis")
print("Mean Salary:",round(statistics.mean(salaries),2))
print("Variance:",round(salary_variance,2))
print("Standard Deviation:",round(salary_sd,2))
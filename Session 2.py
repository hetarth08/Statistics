import statistics

#Task 1:Calculate mean of Spotify song plays
song_plays=[120,135,150,200,120,90,200]

mean_plays=statistics.mean(song_plays)
print("Mean song plays:",mean_plays)

#Task 2:Find median delivery time
delivery_times=[30,25,40,35,30,45,30]

median_time=statistics.median(delivery_times)
print("Median delivery time:",median_time)

#Task 3:Find the most common product rating
def most_common_rating(ratings):
    return statistics.mode(ratings)

ratings=[5,4,4,3,5,4,2,4]
print("Most common rating:",most_common_rating(ratings))

#Task 4:Compare statistics for three  Youtube Channels
channel1=[100,120,110,105,115,120,100]
channel2=[200,210,205,220,215,210,200]
channel3=[100,120,110,105,5000,100,110]

channels={
    "Channel 1": channel1,
    "Channel 2": channel2,
    "Channel 3": channel3
}

for name, views in channels.items():
    print("\n",name)
    print("Mean:",statistics.mean(views))
    print("Median:",statistics.median(views))
    print("Mode:",statistics.mode(views))

print("\nChannel 3 is most affected by the outlier 5000.")

#Task 5:Analyse a real database using pandas
import pandas as pd

url="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

data=pd.read_csv(url,sep=";")
quality=data["quality"]

print("\nRed Wine Quality Datasets")
print("Mean quality:",quality.mean())
print("Median quality:",quality.median())
print("Mode quality:",quality.mode().iloc[0])
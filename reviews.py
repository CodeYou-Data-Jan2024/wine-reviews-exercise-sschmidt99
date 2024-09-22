#In this exercise we will create a summary of wine reviews by country and write
#the data to a CSV file. This exercise is based on the Kaggle Learn Pandas 
#exercise 3.
#Create a Python program that reads in the `data/winemag-data-130k-v2.csv.zip` 
#file. Create a summary of the data that contains the name, number of reviews, 
#and the average points for each unique country in the dataset. Write the summary
#data to a new file in the `data` folder named `reviews-per-country.csv`.

import pandas as pd

#Read data
wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")
#print(wine_reviews.head())

#For each country create summary of the data that contains the name, number and reviews, and avg
summary = wine_reviews.groupby('country').agg(
    count=('title', 'size'),
    points=('points', 'mean')
).reset_index()

summary['points'] = summary['points'].round(1)

summary.to_csv('data/reviews_per_country.csv', index=False)
import pandas as pd


#Read data
wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")
#wine_reviews.info()
#print('points')
#print(wine_reviews)
#For each country create summary of the data that contains the name, number and reviews, and avg
summary = wine_reviews.groupby('country').agg(
    count=('title', 'size'),
    points=('points', 'mean')
).reset_index()

summary['points'] = summary['points'].round(1)

summary.to_csv('data/reviews_per_country.csv', index=False)
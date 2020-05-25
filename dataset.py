import pandas as pd
from surprise import Dataset
from surprise import Reader

#Read data
games = pd.read_csv("/content/metacritic_critic_reviews.csv")

# Drop columns we dont need
games_data = games.drop(['date','platform','review',],axis=1)


#check the range of metascore
lower_rating = games_data['score'].min()
upper_rating = games_data['score'].max()
print('Review range: {0} to {1}'.format(lower_rating,upper_rating))

#Since we have NaN values we will replace with the average of all scores
final_games = games_data.fillna(games_data.mean(axis=0))

#check if they are gone.
final_games.isnull().values.any()


#First read in the data using the Reader function
reader = Reader(rating_scale=(0, 100))
# The columns must correspond to user id, item id and ratings (in that order). Userscore is not complete.
data = Dataset.load_from_df(final_games[['name', 'game', 'score']], reader)

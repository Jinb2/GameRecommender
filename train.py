from surprise.model_selection import cross_validate
from surprise import accuracy
from surprise import KNNBasic
from surprise.model_selection import KFold
from surprise.model_selection import train_test_split
from dataset import data


# We'll use the famous SVD algorithm.
algo = KNNBasic()
# Run 5-fold cross-validation and print results
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

#Gridsearch CV
from surprise.model_selection import GridSearchCV

param_grid = {'n_epochs': [5, 30], 'lr_all': [0.002, 0.005],
              'reg_all': [0.4, 0.6]}
gs = GridSearchCV(KNNBasic, param_grid, measures=['rmse', 'mae'], cv=5)

gs.fit(data)

# best RMSE score
print(gs.best_score['rmse'])

# combination of parameters that gave the best RMSE score
print(gs.best_params['rmse'])

#set to optimal parameters
algo = gs.best_estimator['rmse']
cross_validate(algo, data, measures=['RMSE'], cv=5, verbose=False)

#Compute how well the model did.
trainset, testset = train_test_split(data, test_size=0.3)
algo = gs.best_estimator['rmse']
predictions = algo.fit(trainset).test(testset)
accuracy.rmse(predictions)

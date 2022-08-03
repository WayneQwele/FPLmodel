print("Hello")


#%%

import pandas as pd

GameWeek1  = pd.read_csv('/Users/nduqwele/Code/GithubProjects/Fantasy-Premier-League/data/2021-22/gws/gw1.csv')  #location of the data
# %%
print(GameWeek1.head())
# %%
# I need to create a queury that extracts best player in every position after every gameweek.
#  we need to recreate what would be a succesfull strategy after every week.
#  we have to bare in mind that we have the constraints : cost of football teamplayers,
# can I create a random team selection? Then calculate costs of such a team? Tournament?, 
# How do i calculate the most optimal team seleaction irrespective of the initial team selection?
# What if we restrict team valuation picks and calculate best team under these cosntraints?
# who is has been the most popular players by transfers by people?
# cumaltive measures by players?
#  

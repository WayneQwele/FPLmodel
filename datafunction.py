
# somewhere to put all the pandas functions and operations.

import pandas as pd

def points(row):
    # for row wise computation
    '''
    This is used to compute Team points over the season
    '''

    if row <-0:
        result = 0
    elif row == 0:
        result = 1
    else:
        result = 3
    return result

def home_away(row):
    '''
    This adds needs to updated description.
    '''
    if row['was_home'] == True:   # this is always frustrating row[(row['was_home'] == True)]
        value =  row['Home']
    else:
        value =  row['Away']
    return value



def adder (el):
    '''
    This another function used points in feature build
    '''

    score = pd.Series(el['team_h_score']-el['team_a_score']).apply(points) # so this will return a  pandas series, our evaluation returns a series. So we need to do our evaluation right over here
    score_a = pd.Series(el['team_a_score']-el['team_h_score']).apply(points) 
    combine = {'Home':score, 'Away':score_a,'was_home':el['was_home']}
    df = pd.DataFrame(combine).apply(home_away,axis=1) #.apply(home_away)

    # if (el['was_home'] == True):
        

    return df

def playtime(row):
    '''
    To clasify playing time for players.
    '''
    if row <5:
        result = 0
    else:
        result = 1
    return result


def total_point_correction(row):
    # for row wise computation
    '''
    This is used to compute Team points over the season
    '''

    if row <-0:
        result = 0
    else:
        result = row
    return result
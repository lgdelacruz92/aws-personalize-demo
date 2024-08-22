import pandas as pd
from aws import boto3
from pprint import pprint

# reading the original data in order to have a dataframe that has both movie_ids 
# and the corresponding titles to make out recommendations easier to read.
items_df = pd.read_csv('./ml-latest-small/movies.csv')
items_df.sample(10)

def get_movie_by_id(movie_id, movie_df):
    """
    This takes in an movie_id from a recommendation in string format,
    converts it to an int, and then does a lookup in a specified
    dataframe.
    
    A really broad try/except clause was added in case anything goes wrong.
    
    Feel free to add more debugging or filtering here to improve results if
    you hit an error.
    """
    try:
        return movie_df.loc[movie_df["movieId"]==int(movie_id)]['title'].values[0]
    except:
        print (movie_id)
        return "Error obtaining title"
    


# First pick a user
test_user_id = "1"

# Select a random item
test_item_id = "81847" #Iron Man 59315, Tangled: 81847

recommender_more_like_x_arn = 'arn:aws:personalize:us-east-1:985539775357:recommender/more_like_x_demo'

personalize_runtime = boto3.client('personalize-runtime')
# Get recommendations for the user for this item
get_recommendations_response = personalize_runtime.get_recommendations(
    recommenderArn = recommender_more_like_x_arn,
    userId = test_user_id,
    itemId = test_item_id,
    numResults = 20
)

# Build a new dataframe for the recommendations
item_list = get_recommendations_response['itemList']
recommendation_list = []
for item in item_list:
    movie = get_movie_by_id(item['itemId'], items_df)
    recommendation_list.append(movie)

user_recommendations_df = pd.DataFrame(recommendation_list, columns = [get_movie_by_id(test_item_id, items_df)])

pd.options.display.max_rows = 20
pprint(user_recommendations_df)
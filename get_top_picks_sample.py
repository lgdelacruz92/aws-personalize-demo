from aws import pd, boto3
from pprint import pprint

items_df = pd.read_csv('./ml-latest-small/movies.csv')
items_df.sample(10)

users_data_df = pd.read_csv('./users.csv')

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
    

def get_gender_by_id(user_id, user_df):
    """
    This takes in a user_id and then does a lookup in a specified
    dataframe.
    
    A really broad try/except clause was added in case anything goes wrong.
    
    Feel free to add more debugging or filtering here to improve results if
    you hit an error.
    """
    # return user_df.loc[user_df["USER_ID"]==int(user_id)]['GENDER'].values[0]
    try:
        return user_df.loc[user_df["USER_ID"]==int(user_id)]['GENDER'].values[0]
    except:
        print (user_id)
        return "Error obtaining title"
    
personalize_runtime = boto3.client('personalize-runtime')

recommender_top_picks_arn = 'arn:aws:personalize:us-east-1:985539775357:recommender/top_picks_for_you_demo'
    
# First pick a user
test_user_id = "111" # samples users: 55, 75, 76, 111

# Get recommendations for the user
get_recommendations_response = personalize_runtime.get_recommendations(
    recommenderArn = recommender_top_picks_arn,
    userId = test_user_id,
    numResults = 10
)

# Build a new dataframe for the recommendations
item_list = get_recommendations_response['itemList']
recommendation_list = []
for item in item_list:
    movie = get_movie_by_id(item['itemId'], items_df)
    recommendation_list.append(movie)

column_name = test_user_id+" ("+get_gender_by_id(test_user_id, users_data_df)+")"

user_recommendations_df = pd.DataFrame(recommendation_list, columns = [column_name])

pd.options.display.max_rows =10
pprint(user_recommendations_df)
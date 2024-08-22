from aws import json, boto3, vod_dataset_group_arn as dataset_group_arn
from pprint import pprint

personalize = boto3.client('personalize')

create_recommender_response = personalize.create_recommender(
  name = 'more_like_x_demo',
  recipeArn = 'arn:aws:personalize:::recipe/aws-vod-more-like-x',
  datasetGroupArn = dataset_group_arn
)
recommender_more_like_x_arn = create_recommender_response["recommenderArn"]
pprint (json.dumps(create_recommender_response))
from aws import boto3, json, vod_dataset_group_arn as dataset_group_arn
from pprint import pprint

personalize = boto3.client('personalize')
create_recommender_response = personalize.create_recommender(
  name = 'top_picks_for_you_demo',
  recipeArn = 'arn:aws:personalize:::recipe/aws-vod-top-picks',
  datasetGroupArn = dataset_group_arn
)
recommender_top_picks_arn = create_recommender_response["recommenderArn"]
pprint (json.dumps(create_recommender_response))
# Imports
import boto3
import json
import numpy as np
import pandas as pd
import time
import datetime


# Configure the SDK to Personalize:
personalize = boto3.client('personalize')
personalize_runtime = boto3.client('personalize-runtime')

interactions_data = pd.read_csv('./ml-latest-small/ratings.csv')
pd.set_option('display.max_rows', 5)
# print(interactions_data)

interactions_data = interactions_data[interactions_data['rating'] > 3]                # Keep only movies rated higher than 3 out of 5.
interactions_data = interactions_data[['userId', 'movieId', 'timestamp']]
interactions_data.rename(columns = {'userId':'USER_ID', 'movieId':'ITEM_ID', 
                              'timestamp':'TIMESTAMP'}, inplace = True)
interactions_data['EVENT_TYPE']='watch' #Adds an EVENT_TYPE column and an event type of "watch" for each interaction.
# interactions_data.head()

items_data = pd.read_csv('./ml-latest-small/movies.csv')

items_data['year'] = items_data['title'].str.extract('.*\((.*)\).*',expand = False)
# items_data.head(5)


ts= datetime.datetime(2022, 1, 1, 0, 0).strftime('%s')
items_data["CREATION_TIMESTAMP"] = ts

# removing the title
items_data.drop(columns="title", inplace = True)

# renaming the columns to match schema
items_data.rename(columns = { 'movieId':'ITEM_ID', 'genres':'GENRES',
                              'year':'YEAR'}, inplace = True)

user_ids = interactions_data['USER_ID'].unique()
user_data = pd.DataFrame()
user_data["USER_ID"]=user_ids

possible_genders = ['female', 'male']
random = np.random.choice(possible_genders, len(user_data.index), p=[0.5, 0.5])
user_data["GENDER"] = random

# s3 = boto3.client('s3')
region = 'us-east-1'
account_id = boto3.client('sts').get_caller_identity().get('Account')
bucket_name = account_id + "-" + region + "-" + "personalizemanagedvod"
# print('bucket_name:', bucket_name)

# try:
#     if region == "us-east-1":
#         s3.create_bucket(Bucket=bucket_name)
#     else:
#         s3.create_bucket(
#             Bucket=bucket_name,
#             CreateBucketConfiguration={'LocationConstraint': region}
#             )
# except s3.exceptions.BucketAlreadyOwnedByYou:
#     print("Bucket already exists. Using bucket", bucket_name)

# interactions_filename = "interactions.csv"
# interactions_data.to_csv(interactions_filename, index=False)
# boto3.Session().resource('s3').Bucket(bucket_name).Object(interactions_filename).upload_file(interactions_filename)

# items_filename = "items.csv"
# items_data.to_csv(items_filename, index=False)
# boto3.Session().resource('s3').Bucket(bucket_name).Object(items_filename).upload_file(items_filename)

# user_filename = "users.csv"
# user_data.to_csv(user_filename, index=False)
# boto3.Session().resource('s3').Bucket(bucket_name).Object(user_filename).upload_file(user_filename)

s3 = boto3.client("s3")
# policy = {
#     "Version": "2012-10-17",
#     "Id": "PersonalizeS3BucketAccessPolicy",
#     "Statement": [
#         {
#             "Sid": "PersonalizeS3BucketAccessPolicy",
#             "Effect": "Allow",
#             "Principal": {
#                 "Service": "personalize.amazonaws.com"
#             },
#             "Action": [
#                 "s3:GetObject",
#                 "s3:ListBucket"
#             ],
#             "Resource": [
#                 "arn:aws:s3:::{}".format(bucket_name),
#                 "arn:aws:s3:::{}/*".format(bucket_name)
#             ]
#         }
#     ]
# }

# s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(policy))

# response = personalize.create_dataset_group(
#     name='personalize-video-on-demand-ds-group',
#     domain='VIDEO_ON_DEMAND'
# )

# dataset_group_arn = response['datasetGroupArn']
# print(json.dumps(response, indent=2))

# schema = {
#   "type": "record",
#   "name": "Interactions",
#   "namespace": "com.amazonaws.personalize.schema",
#   "fields": [
#       {
#           "name": "USER_ID",
#           "type": "string"
#       },
#       {
#           "name": "ITEM_ID",
#           "type": "string"
#       },
#       {
#           "name": "EVENT_TYPE",
#           "type": "string"
#       },
#       {
#           "name": "TIMESTAMP",
#           "type": "long"
#       }
#   ],
#   "version": "1.0"
# }

# create_interactions_schema_response = personalize.create_schema(
#     name='personalize-demo-interactions-schema',
#     schema=json.dumps(schema),
#     domain='VIDEO_ON_DEMAND'
# )

# interactions_schema_arn = create_interactions_schema_response['schemaArn']
# print(json.dumps(create_interactions_schema_response, indent=2))

# schema = {
#   "type": "record",
#   "name": "Items",
#   "namespace": "com.amazonaws.personalize.schema",
#   "fields": [
#     {
#       "name": "ITEM_ID",
#       "type": "string"
#     },
#     {
#       "name": "GENRES",
#       "type": [
#         "string"
#       ],
#       "categorical": True
#     },
#     {
#       "name": "YEAR",
#       "type": [
#         "string"
#       ],
#       "categorical": True
#     }, 
#     {
#       "name": "CREATION_TIMESTAMP",
#       "type": "long"
#     }
#   ],
#   "version": "1.0"
# }
# create_items_schema_response = personalize.create_schema(
#     name='personalize-demo-items-schema',
#     schema=json.dumps(schema),
#     domain='VIDEO_ON_DEMAND'
# )

# items_schema_arn = create_items_schema_response['schemaArn']
# print(json.dumps(create_items_schema_response, indent=2))

schema = {
    "type": "record",
    "name": "Users",
    "namespace": "com.amazonaws.personalize.schema",
    "fields": [
      {
          "name": "USER_ID",
          "type": "string"
      },
      {
          "name": "GENDER",
          "type": "string",
          "categorical": True
      }
    ],
    "version": "1.0"
}
create_users_schema_response = personalize.create_schema(
    name='personalize-demo-users-schema',
    schema=json.dumps(schema),
    domain='VIDEO_ON_DEMAND'
)

users_schema_arn = create_users_schema_response['schemaArn']
print(json.dumps(create_users_schema_response, indent=2))
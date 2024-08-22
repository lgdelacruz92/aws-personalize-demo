import boto3
import json

personalize = boto3.client('personalize')

role_arn = 'arn:aws:iam::985539775357:role/PersonalizeRoleVODDemoRecommender'
users_dataset_arn = 'arn:aws:personalize:us-east-1:985539775357:dataset/personalize-video-on-demand-ds-group/USERS'
bucket_name = '985539775357-us-east-1-personalizemanagedvod'
users_filename = 'users.csv'

create_users_dataset_import_job_response = personalize.create_dataset_import_job(
    jobName = "personalize-demo-import-users",
    datasetArn = users_dataset_arn,
    dataSource = {
        "dataLocation": "s3://{}/{}".format(bucket_name, users_filename)
    },
    roleArn = role_arn
)

dataset_users_import_job_arn = create_users_dataset_import_job_response['datasetImportJobArn']
print(json.dumps(create_users_dataset_import_job_response, indent=2))
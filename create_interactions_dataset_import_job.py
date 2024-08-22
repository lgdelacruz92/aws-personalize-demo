import boto3
import json

personalize = boto3.client('personalize')

role_arn = 'arn:aws:iam::985539775357:role/PersonalizeRoleVODDemoRecommender'
interactions_dataset_arn = 'arn:aws:personalize:us-east-1:985539775357:dataset/personalize-video-on-demand-ds-group/INTERACTIONS'
bucket_name = '985539775357-us-east-1-personalizemanagedvod'
interactions_filename = 'interactions.csv'

create_interactions_dataset_import_job_response = personalize.create_dataset_import_job(
    jobName = "personalize-demo-import-interactions",
    datasetArn = interactions_dataset_arn,
    dataSource = {
        "dataLocation": "s3://{}/{}".format(bucket_name, interactions_filename)
    },
    roleArn = role_arn
)

dataset_interactions_import_job_arn = create_interactions_dataset_import_job_response['datasetImportJobArn']
print(json.dumps(create_interactions_dataset_import_job_response, indent=2))
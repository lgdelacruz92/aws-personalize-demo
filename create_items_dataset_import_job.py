import boto3
import json

personalize = boto3.client('personalize')

role_arn = 'arn:aws:iam::985539775357:role/PersonalizeRoleVODDemoRecommender'
items_dataset_arn = 'arn:aws:personalize:us-east-1:985539775357:dataset/personalize-video-on-demand-ds-group/ITEMS'
bucket_name = '985539775357-us-east-1-personalizemanagedvod'
items_filename = 'items.csv'

create_items_dataset_import_job_response = personalize.create_dataset_import_job(
    jobName = "personalize-demo-import-items",
    datasetArn = items_dataset_arn,
    dataSource = {
        "dataLocation": "s3://{}/{}".format(bucket_name, items_filename)
    },
    roleArn = role_arn
)

dataset_items_import_job_arn = create_items_dataset_import_job_response['datasetImportJobArn']
print(json.dumps(create_items_dataset_import_job_response, indent=2))
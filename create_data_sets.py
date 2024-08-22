from aws import personalize
from aws import json

arn_prefix = 'arn:aws:personalize:us-east-1:985539775357'
dataset_group_arn = f'{arn_prefix}:dataset-group/personalize-video-on-demand-ds-group'

def create_interactions_dataset():
    dataset_type = "INTERACTIONS"

    interactions_schema_arn = f'{arn_prefix}:schema/personalize-demo-interactions-schema'

    create_dataset_response = personalize.create_dataset(
        name = "personalize-demo-interactions",
        datasetType = dataset_type,
        datasetGroupArn = dataset_group_arn,
        schemaArn = interactions_schema_arn
    )

    interactions_dataset_arn = create_dataset_response['datasetArn']
    print(json.dumps(create_dataset_response, indent=2))

def create_items_dataset():
    dataset_type = "ITEMS"
    items_schema_arn = f'{arn_prefix}:schema/personalize-demo-items-schema'

    create_dataset_response = personalize.create_dataset(
        name = "personalize-demo-items",
        datasetType = dataset_type,
        datasetGroupArn = dataset_group_arn,
        schemaArn = items_schema_arn
    )

    items_dataset_arn = create_dataset_response['datasetArn']
    print(json.dumps(create_dataset_response, indent=2))

def create_users_dataset():
    dataset_type = "USERS"
    users_schema_arn = f'{arn_prefix}:schema/personalize-demo-users-schema'

    create_dataset_response = personalize.create_dataset(
        name = "personalize-demo-users",
        datasetType = dataset_type,
        datasetGroupArn = dataset_group_arn,
        schemaArn = users_schema_arn
    )

    users_dataset_arn = create_dataset_response['datasetArn']
    print(json.dumps(create_dataset_response, indent=2))
if __name__ == '__main__':
    create_users_dataset()
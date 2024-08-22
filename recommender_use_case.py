import boto3
from pprint import pprint
personalize = boto3.client('personalize')

available_recipes = personalize.list_recipes(domain='VIDEO_ON_DEMAND') # See a list of recommenders for the domain. 
if (len(available_recipes["recipes"])==0):
    # This is a workaround to get the recipes in case 'available_recipes["recipes"]'does not retrieve them
    available_recipes = personalize.list_recipes(domain='VIDEO_ON_DEMAND', nextToken=available_recipes["nextToken"])

for recipe in available_recipes['recipes']:
    name = recipe['name']
    arn = recipe['recipeArn']

    print(f'name: {name}, arn: {arn}\n')

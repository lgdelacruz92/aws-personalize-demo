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

vod_dataset_group_arn = 'arn:aws:personalize:us-east-1:985539775357:dataset-group/personalize-video-on-demand-ds-group'
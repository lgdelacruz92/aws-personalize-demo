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
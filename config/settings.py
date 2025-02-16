import os

from dotenv import load_dotenv

load_dotenv()

HUBSPOT_API_KEY = os.getenv('HUBSPOT_API_KEY')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_PROD_URL = 'https://l0hefgbbla.execute-api.us-east-1.amazonaws.com/prod'
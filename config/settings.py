import os

from dotenv import load_dotenv

load_dotenv()

# Keys
HUBSPOT_API_KEY = os.getenv('HUBSPOT_API_KEY')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')

# Endpoints
AWS_PROD_URL = os.getenv('AWS_PROD_URL')

# Limits
MAX_WORKERS = 10
HUBSPOT_CREATE_CONTACT_BATCH_SIZE = 100
RATE_LIMIT_MAX_RETRIES = 5
RATE_LIMIT_BASE_WAIT = 10

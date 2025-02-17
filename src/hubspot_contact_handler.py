from hubspot import HubSpot
from utils.batch_processing import create_hubspot_batch_input
from utils.rate_limit_utils import retry_on_rate_limit
from config.settings import HUBSPOT_API_KEY
from config.logger import logger

class HubSpotContactHandler:

    def __init__(self):
        self.client = HubSpot()
        self.client.access_token = HUBSPOT_API_KEY

    @retry_on_rate_limit
    def upsert_contacts(self, contacts):
        batch_input = create_hubspot_batch_input(contacts)
        api_response = self.client.crm.contacts.batch_api.upsert(batch_input)
        logger.info(f"Successfully upserted {len(batch_input.inputs)} contacts in HubSpot.")
        return api_response.to_dict()

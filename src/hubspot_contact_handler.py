import time

from hubspot import HubSpot
from hubspot.crm.contacts import BatchInputSimplePublicObjectBatchInputUpsert, SimplePublicObjectBatchInput
from hubspot.crm.contacts.exceptions import ApiException
from config.logger import logger
from config.settings import HUBSPOT_API_KEY, RATE_LIMIT_MAX_RETRIES, RATE_LIMIT_BASE_WAIT

class HubSpotContactHandler:

    def __init__(self):
        self.client = HubSpot()
        self.client.access_token = HUBSPOT_API_KEY

    def upsert_contacts(self, contacts):
        batch_input = self.create_batch_input(contacts)

        for attempt in range(RATE_LIMIT_MAX_RETRIES):
            try:
                api_response = self.client.crm.contacts.batch_api.upsert(batch_input)
                return api_response.to_dict()
            except ApiException as e:
                if e.status == 429:
                    wait_time = RATE_LIMIT_BASE_WAIT * (2 ** attempt)
                    logger.warning(f"Rate limit reached. Retrying in {wait_time:.2f} seconds... (Attempt {attempt + 1}/{RATE_LIMIT_MAX_RETRIES})")
                    time.sleep(wait_time)
                else:
                    return {"error": f"ApiException: {e}"}

        return {"error": "Max retries reached. Failed to upsert contacts.."}

    def create_batch_input(self, contacts):
        return BatchInputSimplePublicObjectBatchInputUpsert(
            inputs=[
                SimplePublicObjectBatchInput(
                    id_property="email",
                    id=contact["email"],
                    properties={
                        "firstname": contact["first_name"],
                        "lastname": contact["last_name"],
                        "phone": contact["phone_number"],
                        "gender": contact["gender"]
                    }
                ) for contact in contacts
            ]
        )

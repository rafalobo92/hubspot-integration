from src.hubspot_contact_handler import HubSpotContactHandler
from src.aws_contact_handler import AWSContactHandler
from config.logger import logger
from config.settings import MAX_WORKERS, HUBSPOT_CREATE_CONTACT_BATCH_SIZE
from concurrent.futures import ThreadPoolExecutor, as_completed

class ContactSyncService:

    def __init__(self):
        self.aws_contact_handler = AWSContactHandler()
        self.hubspot_contact_handler = HubSpotContactHandler()

    def sync(self, quantity):
        aws_contacts = self.aws_contact_handler.fetch_contacts()
        if not aws_contacts:
            logger.info("No contacts to sync.")
            return

        contacts_to_import = aws_contacts[:quantity]
        batch_contacts = self.create_batch_contacts(contacts=contacts_to_import)

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {executor.submit(self.hubspot_contact_handler.upsert_contacts, batch): batch for batch in batch_contacts}
            for future in as_completed(futures):
                batch = futures[future]
                try:
                    response = future.result()
                    if "error" in response:
                        logger.error(f"Error upserting contacts in HubSpot: {response['error']}")
                    else:
                        logger.info(f"Successfully upserted {len(batch)} contacts in HubSpot.")
                except Exception as e:
                    logger.error(f"Exception upserting contacts in HubSpot: {e}")

    def create_batch_contacts(self, contacts):
        return [
            contacts[i : i + HUBSPOT_CREATE_CONTACT_BATCH_SIZE]
            for i in range(0, len(contacts), HUBSPOT_CREATE_CONTACT_BATCH_SIZE)
        ]

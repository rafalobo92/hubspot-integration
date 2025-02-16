from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInput, SimplePublicObjectInputForCreate
from hubspot.crm.contacts.exceptions import ApiException
from config.settings import HUBSPOT_API_KEY

class HubSpotContactHandler:
    def __init__(self):
        self.client = HubSpot()
        self.client.access_token = HUBSPOT_API_KEY
    
    def get_contacts(self, count=10):
        try:
            api_response = self.client.crm.contacts.basic_api.get_page(limit=count)
            return [contact.to_dict() for contact in api_response.results]
        except ApiException as e:
            return {"error": f"Exception when calling HubSpot API: {e}"}
    
    def create_contact(self, properties):
        contact_input = SimplePublicObjectInputForCreate(properties=properties)
        try:
            api_response = self.client.crm.contacts.basic_api.create(contact_input)
            return api_response.to_dict()
        except ApiException as e:
            return {"error": f"Exception when creating contact: {e}"}
    
    def update_contact(self, contact_id, properties):
        contact_input = SimplePublicObjectInput(properties=properties)
        try:
            api_response = self.client.crm.contacts.basic_api.update(contact_id, contact_input)
            return api_response.to_dict()
        except ApiException as e:
            return {"error": f"Exception when updating contact: {e}"}

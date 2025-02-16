from src.hubspot_contact_handler import HubSpotContactHandler
from src.aws_contact_handler import AWSContactHandler

class ContactSyncService:
    def __init__(self):
        self.aws_contact_handler = AWSContactHandler()
        self.hubspot_contact_handler = HubSpotContactHandler()

    def sync(self, quantity):
        aws_contacts = self.aws_contact_handler.fetch_contacts()
        if aws_contacts:
            contacts_to_import = aws_contacts[:quantity]
            for contact in contacts_to_import:
                self.create_contact_in_hubspot(contact)
        else:
            print("No contacts to sync.")

    def create_contact_in_hubspot(self, contact):
        data = {
            "firstname": contact["first_name"],
            "lastname": contact["last_name"],
            "email": contact["email"],
            "phone": contact["phone_number"],
            "gender": contact["gender"]
        }
        response = self.hubspot_contact_handler.create_contact(data)
        if "error" in response:
            print(f"Error creating contact {contact['first_name']} {contact['last_name']} in HubSpot: {response['error']}")
        else:
            print(f"Contact {contact['first_name']} {contact['last_name']} created successfully into HubSpot.")
